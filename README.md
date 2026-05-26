# Whisper Transcriptor DPI

Aplicacion de escritorio local para transcribir audio/video con OpenAI Whisper.

## Version

v1.8 P/R editable

## Funciones principales

- Carga de audio o video.
- Seleccion de modelo Whisper: tiny, base, small, medium, large, turbo.
- Seleccion de idioma automatico o manual.
- Transcripcion o traduccion al ingles.
- Optimizacion previa con FFmpeg.
- Control de hilos CPU/FFmpeg.
- Troceo de archivos largos.
- Formato normal, P/R alternado simple y P/R inteligente llamada.
- Bloques PREGUNTA/RESPUESTA editables desde la interfaz.
- Exportacion a TXT, SRT, VTT, JSON y Word.

## Instalar dependencias

Ejecutar:

```bat
install_dependencies.bat
```

## Instalar FFmpeg

Ejecutar:

```bat
install_ffmpeg_winget.bat
```

## Ejecutar la app

```bat
run_app.bat
```

## Compilar EXE

```bat
build_windows.bat
```

El ejecutable queda en:

```text
dist\WhisperTranscriptorDPI.exe
```

## Recomendacion de uso

Para llamadas o entrevistas breves:

- Modelo: small
- Idioma: Espanol
- Formato: P/R inteligente llamada
- Rendimiento: Rapido o Equilibrado
- Hilos: Auto
- Trocear: 10 min o 15 min
- Limpieza policial basica: activada

Luego corregir los bloques desde el panel derecho con los botones PREGUNTA/RESPUESTA.
