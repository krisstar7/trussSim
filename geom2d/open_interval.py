from geom2d.nums import are_close_enough

class OpenInterval:
    def __init__(self, start: float, end: float):
        if start > end:
            raise ValueError('start should be smaller than end')
        self.start = start
        self.end = end

    @property
    def length(self):
        return self.end - self.start
    
    def contains(self, value):
        return self.start < value < self.end
    
    def overlaps_interval(self, other):
        if are_close_enough(self.start, other.start) and are_close_enough(self.end, other.end):
            return True
        
        return self.contains(other.start) \
            or self.contains(other.end) \
            or other.contains(self.start) \
            or other.contains(self.end)
    
    def compute_overlap_with(self, other):
        if not self.overlaps_interval(other):
            return None
        
        return OpenInterval(max(self.start, other.start), min(self.end, other.end))
    
    