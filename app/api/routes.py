from fastapi import APIRouter, HTTPException
from app.services.diagnostic_model import SymptomInput
from app.services.diagnostic_model import get_diagnosis_from_llm

router = APIRouter()

@router.post("/diagnostico")
def diagnostico(input: SymptomInput):
    result = get_diagnosis_from_llm(input.sintomas)
    if not result:
        raise HTTPException(status_code=500, detail="Erro ao gerar diagnóstico")
    return {"resposta": result}
