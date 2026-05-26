@echo off
setlocal EnableExtensions
cd /d "%~dp0"

echo ================================================
echo  Whisper Transcriptor DPI - Installer
echo ================================================
echo.

set "PY_CMD="

py -3.11 --version >nul 2>nul
if not errorlevel 1 set "PY_CMD=py -3.11"

if not defined PY_CMD (
    py -3 --version >nul 2>nul
    if not errorlevel 1 set "PY_CMD=py -3"
)

if not defined PY_CMD (
    python --version >nul 2>nul
    if not errorlevel 1 set "PY_CMD=python"
)

if not defined PY_CMD (
    python3 --version >nul 2>nul
    if not errorlevel 1 set "PY_CMD=python3"
)

if not defined PY_CMD (
    echo ERROR: Python was not found.
    echo.
    echo Recommended fix:
    echo 1^) Install Python 3.11 64-bit.
    echo 2^) During install, check: Add python.exe to PATH.
    echo 3^) Close this window and open a new one.
    echo 4^) Run install_dependencies.bat again.
    echo.
    echo Optional install with winget:
    echo winget install -e --id Python.Python.3.11
    echo.
    echo If Windows opens Microsoft Store, disable the aliases:
    echo Settings ^> Apps ^> Advanced app settings ^> App execution aliases
    echo Turn off python.exe and python3.exe.
    echo.
    pause
    exit /b 1
)

echo Python detected:
%PY_CMD% --version
if errorlevel 1 (
    echo ERROR: Python command failed.
    pause
    exit /b 1
)

echo.
echo Creating virtual environment .venv ...
%PY_CMD% -m venv .venv
if errorlevel 1 (
    echo.
    echo ERROR: Could not create the virtual environment.
    echo Try installing Python 3.11 from python.org and check Add python.exe to PATH.
    pause
    exit /b 1
)

echo Activating virtual environment ...
call ".venv\Scripts\activate.bat"
if errorlevel 1 (
    echo.
    echo ERROR: Could not activate the virtual environment.
    pause
    exit /b 1
)

echo.
echo Updating pip ...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo.
    echo ERROR: pip update failed.
    pause
    exit /b 1
)

echo.
echo Installing project dependencies ...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo ERROR: Dependency installation failed.
    echo Check your internet connection and try again.
    pause
    exit /b 1
)

echo.
where ffmpeg >nul 2>nul
if errorlevel 1 (
    echo WARNING: FFmpeg was not detected in PATH.
    echo The app can open, but Whisper needs FFmpeg to process audio/video.
    echo You can install it with:
    echo winget install -e --id Gyan.FFmpeg
    echo Or run: install_ffmpeg_winget.bat
    echo.
) else (
    echo FFmpeg detected.
)

echo.
echo Dependencies installed successfully.
echo Run the app with: run_app.bat
echo.
pause
exit /b 0
