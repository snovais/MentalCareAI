import openai
from app.core.config import OPENAI_API_KEY
from app.core.utils import create_prompt

openai.api_key = OPENAI_API_KEY

def get_diagnosis_from_llm(symptoms: str) -> str:
    prompt = create_prompt(symptoms)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Assistente clínico experiente em saúde mental."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=400
    )
    return response["choices"][0]["message"]["content"]
