FROM python:3.12-slim
LABEL authors="pplevins & berale"
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY app/services/data_retrieval/data_retrieval_service.py ./data_retrieval/data_retrieval_service.py
COPY app/services/data_retrieval/__init__.py ./data_retrieval/__init__.py
COPY app/core ./core
COPY app/dal ./dal
COPY app/api ./api
COPY app/tests/data_retrieval_main.py data_retrieval_main.py
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["python", "data_retrieval_main.py"]