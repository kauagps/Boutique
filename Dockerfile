FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY wait-for-it.sh /wait-for-it.sh
COPY docker-entrypoint.sh /docker-entrypoint.sh

# Torna os scripts executáveis e aplica dos2unix
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential \
    dos2unix && \
    dos2unix /wait-for-it.sh && \
    dos2unix /docker-entrypoint.sh && \
    chmod +x /wait-for-it.sh /docker-entrypoint.sh

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/docker-entrypoint.sh"]
