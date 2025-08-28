FROM python:3.12-slim
LABEL authors="pplevins & berale"
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY app/services/persister/persister_service.py ./persister/persister_service.py
COPY app/services/persister/__init__.py ./persister/__init__.py
COPY app/core ./core
COPY app/dal ./dal
COPY app/models ./models
COPY app/tests/persister_main.py persister_main.py
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "persister_main.py"]