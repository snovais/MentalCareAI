import streamlit as st
import requests

st.title("MentalCareAI - Diagnóstico Rápido")

sintomas = st.text_area("Digite os sintomas do paciente:")

if st.button("Gerar Diagnóstico"):
    try:
        url = "http://127.0.0.1:8000/diagnostico"
        response = requests.post(url, json={"sintomas": sintomas})
        if response.status_code == 200:
            st.success(response.json()["resposta"])
        else:
            st.error("Erro ao gerar diagnóstico")
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
