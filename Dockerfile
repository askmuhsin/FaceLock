# syntax=docker/dockerfile:1.7
FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1     PIP_NO_CACHE_DIR=1     PATH="/root/.local/bin:${PATH}"

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends     curl ca-certificates build-essential     && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY app ./app
COPY static ./static

ENV APP_NAME="Private Face ID"
ENV APP_SEED="prod-seed-change-me"
ENV PORT=8000

EXPOSE 8000

CMD ["python", "-m", "app.main"]
