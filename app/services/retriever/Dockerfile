FROM python:3.12-slim
LABEL authors="pplevins & berale"
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY app/services/retriever/retriever_manager.py ./retriever/retriever_manager.py
COPY app/services/retriever/retriever_service.py ./retriever/retriever_service.py
COPY app/services/retriever/__init__.py ./retriever/__init__.py
COPY app/core ./core
COPY app/dal ./dal
COPY app/models ./models
COPY app/tests/retriever_main.py retriever_main.py
COPY app/services/retriever/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV MONGODB_DATABASE="IranMalDB" \
    MONGODB_URL="mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/"
CMD ["python", "retriever_main.py"]