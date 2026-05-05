import os
from sqlalchemy import create_engine
from alembic import context

target_metadata = None

def run_migrations_offline():
    url = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = create_engine(os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname"))
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()
