@echo off

REM Delete EasierGUI.py if it exists
if exist EasierGUI.py (
    del EasierGUI.py
)

mkdir audios

runtime\python.exe install_easy_dependencies.py

pause