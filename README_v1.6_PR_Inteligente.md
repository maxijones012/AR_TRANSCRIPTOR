# Whisper Transcriptor DPI - v1.6 P/R inteligente

Esta version corrige el problema del P/R alternado que mezclaba voces cuando Whisper separaba el audio en segmentos muy cortos.

## Novedades

- Nuevo formato: **P/R inteligente llamada**.
- Mantiene el formato viejo: **P/R alternado simple**, solo para borrador rapido.
- Nueva opcion: **Limpieza basica policial: repeticiones y frases comunes**.
- Corrige algunas frases frecuentes mal reconocidas, por ejemplo:
  - "Policia de Tralon" -> "Policia de Trelew".
  - "Sopezido" -> "¿Su apellido?".
- Reduce repeticiones sospechosas cuando Whisper repite una frase corta al final por ruido, silencio o audio no claro.
- Agrega observaciones automaticas para que no se tome como transcripcion final sin revisar.

## Recomendado para llamadas

- Modelo: small
- Idioma: Espanol
- Tarea: Transcribir
- Formato: P/R inteligente llamada
- Rendimiento: Rapido o Equilibrado
- Optimizar audio/video: activado
- Hilos CPU/FFmpeg: Auto
- Trocear archivo: 10 min o 15 min
- Limpieza basica policial: activada

## Importante

Whisper no hace diarizacion real de hablantes. Esta version usa reglas para estimar operador/requirente y agrupar frases, pero siempre hay que revisar escuchando el audio original, especialmente nombres, apellidos, domicilios, horarios y frases dudosas.
