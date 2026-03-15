import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


def extract_document_data(image):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = """
    Actúa como un sistema experto en procesamiento de facturas.

    Analiza la imagen del documento y devuelve únicamente un JSON
    con la siguiente estructura:

    {
      "proveedor": "",
      "fecha": "",
      "numero_documento": "",
      "items": [
        {
          "descripcion": "",
          "cantidad": "",
          "precio": ""
        }
      ],
      "monto_total": ""
    }

    No agregues texto adicional.
    """

    response = model.generate_content([prompt, image])

    return response.text