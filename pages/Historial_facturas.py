import streamlit as st
import pandas as pd

from services.supabase_service import get_invoices

st.title("📊 Historial de Facturas")

data = get_invoices()

if data:

    df = pd.DataFrame(data)

    st.dataframe(df)

else:

    st.info("No hay facturas registradas.")