from supabase import create_client
import streamlit as st

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)


def save_invoice(data):

    response = supabase.table("facturas").insert({
        "proveedor": data["proveedor"],
        "fecha": data["fecha"],
        "numero_documento": data["numero_documento"],
        "monto_total": data["monto_total"],
        "items": data["items"]
    }).execute()

    print(response)

    return response

def get_invoices():

    response = supabase.table("facturas").select("*").order("created_at", desc=True).execute()

    return response.data