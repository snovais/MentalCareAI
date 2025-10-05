from fastapi import APIRouter, HTTPException
from app.models.diagnostico_model import SymptomInput
from app.services.diagnostico_service import get_diagnosis_from_llm

router = APIRouter()

@router.post("/diagnostico")
def diagnostico(input: SymptomInput):
    result = get_diagnosis_from_llm(input.sintomas)
    if not result:
        raise HTTPException(status_code=500, detail="Erro ao gerar diagnóstico")
    return {"resposta": result}
