ARG PYTHON_VERSION=3.12.4
FROM python:${PYTHON_VERSION}-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE 8080

CMD python -m main