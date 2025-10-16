import streamlit as st
import requests

st.title("🧠 MentalCareAI – Diagnóstico Clínico")

texto = st.text_area("Descreva o caso clínico do paciente:")

if st.button("Analisar"):
    with st.spinner("Analisando..."):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/diagnostico",  # <- importante!
                json={"sintomas": texto},
                timeout=60
            )
            if response.status_code == 200:
                st.success(response.json()["resposta"])
            else:
                st.error(f"Erro da API ({response.status_code}): {response.text}")
        except Exception as e:
            st.error(f"Erro de conexão: {e}")
            