# Whisper Transcriptor DPI - v1.5 Hilos y rendimiento

Mejoras principales:

- Hilo de trabajo separado para que la interfaz no se congele.
- Control de hilos CPU/FFmpeg: Auto o manual 1 a 16.
- FFmpeg usa la cantidad de hilos seleccionada.
- PyTorch/Whisper ajusta hilos CPU con `torch.set_num_threads`.
- Troceo opcional del archivo cada 10, 15 o 30 minutos.
- Mejor progreso por fragmentos y cancelacion entre fragmentos.
- Caché de modelo: al usar el mismo modelo de nuevo, no lo recarga.
- Exporta metadatos de hilos y troceo en TXT/Word.

Configuracion recomendada para empezar:

```text
Modelo: small
Idioma: Espanol
Tarea: Transcribir
Rendimiento: Rapido
Dispositivo: Automatico
Optimizar audio/video: activado
Hilos CPU/FFmpeg: Auto
Trocear archivo: 15 min
```

Para PC floja:

```text
Modelo: base
Rendimiento: Rapido
Hilos CPU/FFmpeg: Auto
Trocear archivo: 10 o 15 min
```

Para mejor precision:

```text
Modelo: medium
Rendimiento: Equilibrado
Trocear archivo: 15 o 30 min
```

Notas:

- La transcripcion de un fragmento no se puede cortar instantaneamente porque Whisper queda procesando internamente; la cancelacion responde entre fragmentos.
- No conviene lanzar muchas transcripciones en paralelo con el mismo equipo porque cada proceso cargaria modelos pesados en memoria.
- Si tenes GPU NVIDIA con CUDA funcionando, elegi GPU CUDA. En la mayoria de notebooks comunes, dejalo en Automatico o CPU.
