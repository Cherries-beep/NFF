
FROM python:3.12-slim

WORKDIR /app
# app - рабочая директория внутри контейнера

# устанавливаем poetry
RUN pip install poetry

# копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock* /app/

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Копируем исходный код
COPY src/notes_fastapi /app/notes_fastapi
COPY alembic /app/alembic
COPY alembic.ini /app/
COPY .env /app/

EXPOSE 8000

CMD ["uvicorn", "notes_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
