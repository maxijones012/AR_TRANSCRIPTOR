# Whisper Transcriptor DPI - v1.4 Rendimiento

Aplicacion de escritorio local para transcribir audio/video con OpenAI Whisper.

## Mejoras de rendimiento v1.4

- Cache de modelo: el modelo queda cargado durante la sesion, por lo que la segunda transcripcion con el mismo modelo arranca mas rapido.
- Perfil de rendimiento:
  - Rapido: menor demora, ideal para prueba y videos largos.
  - Equilibrado: punto medio.
  - Preciso: mas lento, mejor para entrevistas importantes.
- Seleccion de dispositivo:
  - Automatico.
  - CPU.
  - GPU CUDA, si el equipo tiene placa NVIDIA compatible y PyTorch con CUDA.
- Optimizacion previa de audio/video:
  - Convierte temporalmente el archivo a WAV mono 16 kHz.
  - Ayuda con videos pesados y formatos raros.
  - No modifica el archivo original.
- Exportaciones TXT, SRT, VTT, JSON y Word mantienen metadatos de rendimiento.

## Uso recomendado

Para empezar en una PC normal:

- Modelo: small
- Idioma: Espanol
- Tarea: Transcribir
- Formato: Texto normal o Entrevista P/R automatica
- Rendimiento: Rapido
- Dispositivo: Automatico
- Optimizar audio/video: activado

Para entrevistas importantes:

- Modelo: medium, si la PC lo soporta.
- Rendimiento: Equilibrado o Preciso.

Si anda lento:

- Usar modelo base o tiny.
- Usar Rendimiento: Rapido.
- Dejar Idioma en Espanol, no Automatico.
- Dejar activada la optimizacion de audio/video.

## Instalacion

1. Ejecutar:

```bat
install_python_311_winget.bat
```

2. Cerrar la ventana y abrir una terminal nueva.

3. Ejecutar:

```bat
install_dependencies.bat
```

4. Instalar FFmpeg:

```bat
install_ffmpeg_winget.bat
```

5. Ejecutar la app:

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

## Importante

El modo P/R automatico es un borrador. Whisper no identifica hablantes por si solo, por lo que debe revisarse manualmente antes de usarlo en actuaciones formales.
