FROM python:3.12-slim
LABEL authors="pplevins & berale"
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY app/services/enricher/enricher_manager.py ./enricher/enricher_manager.py
COPY app/services/enricher/enricher_service.py ./enricher/enricher_service.py
COPY app/services/enricher/__init__.py ./enricher/__init__.py
COPY app/utils/ ./utils
COPY app/models ./models
COPY data ./data
COPY app/tests/enricher_main.py enricher_main.py
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "enricher_main.py"]