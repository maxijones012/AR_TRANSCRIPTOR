# Whisper Transcriptor DPI v1.9 - UI + velocidad

## Cambios principales

- Se agrego motor `Faster Whisper`, pensado para mejorar mucho la velocidad en CPU.
- Se mantiene `OpenAI Whisper oficial` como alternativa.
- Nueva opcion `Precision`:
  - Auto: usa int8 en CPU y float16 en GPU.
  - int8 CPU rapido: recomendado para equipos comunes sin GPU NVIDIA.
  - float16 GPU: recomendado si hay placa NVIDIA compatible.
  - float32 compatible: mas pesado, pero puede servir si int8/float16 fallan.
- Se agregaron etiquetas editables para P/R:
  - Etiqueta 1: por defecto PREGUNTA.
  - Etiqueta 2: por defecto RESPUESTA.
  - Se puede cambiar a OPERADOR / LLAMANTE, ENTREVISTADOR / ENTREVISTADO, etc.
- Al cambiar las etiquetas, los bloques P/R se actualizan solos.
- Los botones de marcado usan el nombre que escribas.

## Configuracion recomendada para velocidad

Modelo: small
Idioma: Espanol
Tarea: Transcribir
Formato: P/R inteligente llamada
Rendimiento: Rapido
Dispositivo: Automatico
Motor: Faster Whisper (mas rapido)
Precision: Auto o int8 CPU rapido
Hilos: Auto
Trocear: 10 min
Optimizar audio/video: activado

## Uso

1. Ejecutar `install_dependencies.bat`.
2. Ejecutar `install_ffmpeg_winget.bat` si no tenes FFmpeg.
3. Ejecutar `run_app.bat`.

## Compilar EXE

Ejecutar:

```bat
build_windows.bat
```

El ejecutable queda en `dist\WhisperTranscriptorDPI.exe`.
