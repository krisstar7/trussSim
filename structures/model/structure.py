from functools import reduce

from eqs import Matrix, Vector as EqVector, cholesky_solve
from .node import StrNode
from .bar import StrBar
from geom2d import Vector
from structures.solution.bar import StrBarSolution
from structures.solution.node import StrNodeSolution
from structures.solution.structure import StructureSolution

class Structure:
    __DOF_PER_NODE = 2

    def __init__(self, nodes: [StrNode], bars: [StrBar]):
        self.__bars = bars
        self.__nodes = nodes

        self.__dofs_dict = None
        self.__system_matrix: Matrix = None
        self.__system_vector: EqVector = None
        self.__global_displacements: EqVector = None

    @property
    def nodes_count(self):
        return len(self.__nodes)
    
    @property
    def bars_count(self):
        return len(self.__bars)
    
    @property
    def loads_count(self):
        return reduce(
            lambda count, node: count + node.loads_count,
            self.__nodes,
            0
        )
    
    def solve_structure(self):
        self.__assign_degrees_of_freedom()
        self.__solve_system_of_equations()
        return self.__make_structure_solution()
    
    def __assign_degrees_of_freedom(self):
        self.__dofs_dict = {}
        for i, node in enumerate(self.__nodes):
            self.__dofs_dict[node.id] = (2 * i, 2 * i + 1)

    def __solve_system_of_equations(self):
        size = self.nodes_count * self.__DOF_PER_NODE
        self.__assemble_system_matrix(size)
        self.__assemble_system_vector(size)
        self.__apply_external_constraints()
        self.__global_displacements = cholesky_solve(
            self.__system_matrix,
            self.__system_vector
        )

    def __assemble_system_matrix(self, size: int):
        matrix = Matrix(size, size)

        for bar in self.__bars:
            bar_matrix = bar.global_stiffness_matrix()
            dofs = self.__bar_dofs(bar)

            for row, row_dof in enumerate(dofs):
                for col, col_dof in enumerate(dofs):
                    matrix.add_to_value(
                        bar_matrix.value_at(row, col),
                        row_dof,
                        col_dof
                    )

        self.__system_matrix = matrix

    def __bar_dofs(self, bar: StrBar):
        start_dofs = self.__dofs_dict[bar.start_node.id]
        end_dofs = self.__dofs_dict[bar.end_node.id]
        return start_dofs + end_dofs
    
    def __assemble_system_vector(self, size: int):
        vector = EqVector(size)

        for node in self.__nodes:
            net_load = node.net_load
            (dof_x, dof_y) = self.__dofs_dict[node.id]

            vector.add_to_value(net_load.u, dof_x)
            vector.add_to_value(net_load.v, dof_y)

        self.__system_vector = vector
    
    def __apply_external_constraints(self):
        for node in self.__nodes:
            (dof_x, dof_y) = self.__dofs_dict[node.id]

            if node.dx_constrained:
                self.__system_matrix.set_identity_row(dof_x)
                self.__system_matrix.set_identity_col(dof_x)
                self.__system_vector.set_value(0, dof_x)

            if node.dy_constrained:
                self.__system_matrix.set_identity_row(dof_y)
                self.__system_matrix.set_identity_col(dof_y)
                self.__system_vector.set_value(0, dof_y)

    def __make_structure_solution(self) -> StructureSolution:
        nodes = [
            self.__node_to_solution(node)
            for node in self.__nodes
        ]

        nodes_dict = {}
        for node in nodes:
            nodes_dict[node.id] = node

        bars = [
            StrBarSolution(
                bar,
                nodes_dict[bar.start_node.id],
                nodes_dict[bar.end_node.id]
            )
            for bar in self.__bars
        ]
        
        return StructureSolution(nodes, bars)
    
    def __node_to_solution(self, node: StrNode) -> StrNodeSolution:
        (dof_x, dof_y) = self.__dofs_dict[node.id]
        disp = Vector(
            self.__global_displacements.value_at(dof_x),
            self.__global_displacements.value_at(dof_y)
        )
        
        return StrNodeSolution(node, disp)
 



