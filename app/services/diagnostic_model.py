from transformers import pipeline
from app.core.utils import create_prompt

# Você pode escolher um modelo melhor abaixo
# Exemplo 1 (leve e rápido): "tiiuae/falcon-7b-instruct"
# Exemplo 2 (muito leve): "mistralai/Mistral-7B-Instruct-v0.2"
# Exemplo 3 (voltado a chat): "HuggingFaceH4/zephyr-7b-beta"

# MODEL_NAME = "tiiuae/falcon-7b-instruct"
# MODEL_NAME = "google/flan-t5-base"

# # Carrega o pipeline de texto
# generator = pipeline(
#     "text-generation",
#     model=MODEL_NAME,
#     torch_dtype="auto",
#     device_map="auto"
# )

# def get_diagnosis_from_llm(symptoms: str) -> str:
#     """
#     Gera diagnóstico baseado nos sintomas informados.
#     """
#     prompt = create_prompt(symptoms)
    
#     response = generator(
#         prompt,
#         max_new_tokens=300,
#         temperature=0.6,
#         do_sample=True,
#         top_p=0.9
#     )

#     output_text = response[0]["generated_text"]

#     # Extrai apenas o diagnóstico gerado, removendo o prompt repetido
#     return output_text[len(prompt):].strip()

from transformers import pipeline

# Carrega o modelo Flan-T5-base (ótimo para tarefas de raciocínio e geração de texto)
modelo = pipeline("text2text-generation", model="./flan-t5-base")

def analisar_texto(texto: str) -> str:
    """
    Analisa o texto do diagnóstico clínico e retorna uma interpretação baseada em sintomas e contexto.
    """
    prompt = (
        "Você é um assistente médico especializado em saúde mental e CAPS-AD. "
        "Analise o seguinte relato clínico e indique o provável diagnóstico entre: "
        "Depressão, Ansiedade, Transtorno Bipolar, Esquizofrenia, Dependência Química, ou Sem indícios de transtorno. "
        "Explique brevemente o motivo. Texto: "
        f"{texto}"
    )

    resultado = modelo(prompt, max_new_tokens=150, temperature=0.7)
    resposta = resultado[0]['generated_text'].strip()
    return resposta

