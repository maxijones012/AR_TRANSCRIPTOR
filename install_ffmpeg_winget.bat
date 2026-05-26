@echo off
setlocal EnableExtensions

echo ================================================
echo  Install FFmpeg with winget
echo ================================================
echo.

where winget >nul 2>nul
if errorlevel 1 (
    echo ERROR: winget was not found on this Windows installation.
    echo Install FFmpeg manually or update App Installer from Microsoft Store.
    echo.
    pause
    exit /b 1
)

winget install -e --id Gyan.FFmpeg
if errorlevel 1 (
    echo.
    echo ERROR: FFmpeg install failed.
    pause
    exit /b 1
)

echo.
echo FFmpeg install completed. Close and reopen the terminal.
echo.
pause
exit /b 0
