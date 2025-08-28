FROM python:3.12-slim
LABEL authors="pplevins & berale"
WORKDIR /app
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY app/services/preprocessor/preprocessor_manager.py ./preprocessor/preprocessor_manager.py
COPY app/services/preprocessor/preprocessor_service.py ./preprocessor/preprocessor_service.py
COPY app/services/preprocessor/__init__.py ./preprocessor/__init__.py
COPY app/utils/text_cleaner.py ./utils/text_cleaner.py
COPY app/models ./models
COPY app/tests/preprocessor_main.py preprocessor_main.py
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "preprocessor_main.py"]