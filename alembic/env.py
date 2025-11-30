"""Главный alembic файл для миграций"""
from __future__ import annotations
import os
import sys
from logging.config import fileConfig

# Добавляем путь к src, чтобы видеть пакет notes_fastapi
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from alembic import context
from sqlalchemy import engine_from_config, pool

# Импорт моделей после настройки sys.path
from notes_fastapi.models import Base

# Alembic Config object
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Метаданные моделей
target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()