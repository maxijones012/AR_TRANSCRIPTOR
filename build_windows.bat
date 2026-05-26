@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ================================================
echo  Whisper Transcriptor DPI - Build EXE
echo ================================================
echo.

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found.
    echo Run install_dependencies.bat first.
    echo.
    pause
    exit /b 1
)

call ".venv\Scripts\activate.bat"
if errorlevel 1 (
    echo ERROR: Could not activate the virtual environment.
    pause
    exit /b 1
)

echo Installing PyInstaller if needed ...
python -m pip install pyinstaller
if errorlevel 1 (
    echo ERROR: Could not install PyInstaller.
    pause
    exit /b 1
)

echo.
echo Building executable ...
pyinstaller --noconfirm --onefile --windowed --name WhisperTranscriptorDPI --collect-all faster_whisper --collect-all ctranslate2 main.py
if errorlevel 1 (
    echo.
    echo ERROR: Build failed.
    pause
    exit /b 1
)

echo.
echo Build complete.
echo EXE location: dist\WhisperTranscriptorDPI.exe
echo.
pause
exit /b 0
