# Whisper Transcriptor DPI v1.3 SafeBAT

Esta version corrige los archivos BAT para Windows.

Cambios:
- BAT sin tildes ni caracteres especiales.
- Deteccion de Python mas segura.
- No informa exito si falla la instalacion.
- Incluye instalador opcional de Python 3.11 por winget.
- Incluye diagnostico_python.bat.

Orden recomendado:
1. Ejecutar install_python_311_winget.bat si Python no esta bien instalado.
2. Cerrar la ventana y abrir otra.
3. Ejecutar install_dependencies.bat.
4. Ejecutar install_ffmpeg_winget.bat.
5. Ejecutar run_app.bat.

Si aparece Microsoft Store al ejecutar python, desactivar:
Settings > Apps > Advanced app settings > App execution aliases > python.exe / python3.exe.

La app usa openai-whisper, PySide6 y python-docx.
