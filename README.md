# AI Invoice Extractor

Sistema de extracción automática de datos desde facturas usando IA multimodal.

## Funcionalidad

La aplicación permite:

1. Subir una imagen de una factura o remito
2. Extraer automáticamente los datos usando IA
3. Estructurar la información en formato JSON
4. Guardar los datos en una base PostgreSQL (Supabase)
5. Consultar el historial de facturas procesadas

## Arquitectura

Imagen de factura
↓
Gemini Vision
↓
Extracción estructurada
↓
Normalización de datos
↓
Supabase Database
↓
Dashboard en Streamlit

## Tecnologías utilizadas

- Python
- Streamlit
- Google Gemini
- Supabase
- Pandas

## Demo del flujo

Factura → IA → JSON → Base de datos → Historial

## Autor

Luis De Gregorio
Ingeniería en Automatización y Control Industrial