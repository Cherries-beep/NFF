""" Главный alembic-файл для подключения к бд, прогрузки моделей, генерации и применения миграций """
from __future__ import annotations
import os
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool # connection pool

from alembic import context

from dotenv import load_dotenv

load_dotenv(".env")

# Импорт моделей
from src.notes_fastapi.models import Base

# Alembic Config object
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# metadata для автогенерации миграций
target_metadata = Base.metadata

def get_url():
    return os.getenv("DATABASE_URL")

def run_migrations_offline():
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    url = get_url()
    # # не использовать пулл соединений - каждый раз создавать новое подключение
    connectable = create_engine(url, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()