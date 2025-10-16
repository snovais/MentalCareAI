import streamlit as st
import requests

st.set_page_config(page_title="MentalCareAI", page_icon="🧠")

st.title("MentalCareAI - Diagnóstico CAPS-AD")
st.markdown("Cole o relato clínico do paciente abaixo e clique em **Analisar**:")

# Caixa de texto para os sintomas
sintomas = st.text_area("Relato clínico:", height=200)

if st.button("Analisar"):
    if sintomas.strip() == "":
        st.warning("Por favor, insira o relato clínico!")
    else:
        with st.spinner("Analisando..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/diagnostico",
                    json={"sintomas": sintomas}
                )
                if response.status_code == 200:
                    resultado = response.json()["diagnostico"]
                    st.success("✅ Diagnóstico gerado:")
                    st.write(resultado)
                else:
                    st.error(f"Erro na API: {response.status_code}")
            except Exception as e:
                st.error(f"Erro de conexão: {e}")
