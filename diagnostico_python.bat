@echo off
setlocal EnableExtensions

echo ================================================
echo  Python diagnosis
echo ================================================
echo.

echo PATH:
echo %PATH%
echo.

echo Checking py launcher:
py --version
py -0p

echo.
echo Checking python:
python --version
where python

echo.
echo Checking pip:
pip --version
where pip

echo.
echo Checking ffmpeg:
ffmpeg -version
where ffmpeg

echo.
pause
exit /b 0
