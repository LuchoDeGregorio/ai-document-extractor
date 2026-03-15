import streamlit as st
from PIL import Image
import pandas as pd

from services.gemini_service import extract_document_data
from utils.json_parser import clean_json_response
from services.supabase_service import save_invoice

# memoria de sesión
if "invoice_data" not in st.session_state:
    st.session_state.invoice_data = None


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

            result_text = extract_document_data(image)

            result_json = clean_json_response(result_text)

            # guardar en memoria
            st.session_state.invoice_data = result_json


# mostrar resultados si existen
if st.session_state.invoice_data:

    st.subheader("Datos extraídos")

    st.json(st.session_state.invoice_data)

    st.subheader("Items")

    df = pd.DataFrame(st.session_state.invoice_data["items"])

    st.table(df)

    # BOTON GUARDAR
    if st.button("Guardar en base de datos"):

        response = save_invoice(st.session_state.invoice_data)

        st.success("Factura guardada en Supabase")

        st.write(response)