# ===== Dockerfile flexível para FastAPI + Streamlit =====
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000 8501

CMD ["bash", "-c", "\
    STREAMLIT_FILE=$(find . -maxdepth 2 -name '*streamlit*.py' -o -name '*app_frontend*.py' | head -n 1) && \
    STREAMLIT_FILE=${STREAMLIT_FILE#./} && \
    echo 'Usando arquivo Streamlit:' $STREAMLIT_FILE && \
    uvicorn app.main:app --host 0.0.0.0 --port 8000 & \
    streamlit run frontend/app_frontend.py --server.port=8501 --server.address=0.0.0.0 \
"]
