@echo off
setlocal EnableExtensions

echo ================================================
echo  Install Python 3.11 with winget
echo ================================================
echo.

where winget >nul 2>nul
if errorlevel 1 (
    echo ERROR: winget was not found.
    echo Download Python 3.11 64-bit from python.org and check Add python.exe to PATH.
    echo.
    pause
    exit /b 1
)

winget install -e --id Python.Python.3.11
if errorlevel 1 (
    echo.
    echo ERROR: Python install failed.
    pause
    exit /b 1
)

echo.
echo Python 3.11 install completed.
echo Close this window and open a new one before running install_dependencies.bat.
echo.
pause
exit /b 0
