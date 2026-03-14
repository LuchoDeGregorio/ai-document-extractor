import streamlit as st
from PIL import Image

from services.gemini_service import extract_document_data

st.title("📄 Extractor Inteligente de Facturas")

st.write("Sube una imagen de factura o remito.")

uploaded_file = st.file_uploader(
    "Seleccionar documento",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="Documento cargado")

    if st.button("Extraer datos"):

        with st.spinner("Analizando documento con IA..."):

            result = extract_document_data(image)

            st.subheader("Datos extraídos")

            st.code(result, language="json")