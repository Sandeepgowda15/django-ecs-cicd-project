FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN groupadd --system django && \
    useradd --system --gid django --home-dir /app django

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=django:django . .

USER django

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "config.wsgi:application"]
