@echo off
chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONPATH=%CD%
python apps\truss_structures\main.py %*
