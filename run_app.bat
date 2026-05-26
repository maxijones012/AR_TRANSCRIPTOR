@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ================================================
echo  Whisper Transcriptor DPI - Run
echo ================================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found.
    echo Run install_dependencies.bat first.
    echo.
    pause
    exit /b 1
)

if not exist "main.py" (
    echo ERROR: main.py was not found in this folder.
    echo Make sure you are running this BAT from the app folder.
    echo.
    pause
    exit /b 1
)

echo Starting app ...
".venv\Scripts\python.exe" "main.py"
if errorlevel 1 (
    echo.
    echo ERROR: The app closed with an error.
    pause
    exit /b 1
)

exit /b 0
