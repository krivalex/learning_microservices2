from typing import Generator
import pytest
from sqlalchemy import Connection, create_engine
from testcontainers.postgres import PostgresContainer

from sql_queries import create_table, insert_transaction
from transaction import Transaction


@pytest.fixture()
def postgres_container1() -> Generator[PostgresContainer, None, None]:
    with PostgresContainer(image="postgres:latest") as container:
        container.start()
        yield container


@pytest.fixture()
def postgres_container() -> PostgresContainer:
    container = PostgresContainer(image="postgres:latest")
    container.start()
    return container


@pytest.fixture()
def postgres_url(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    return postgres_container.get_connection_url()


@pytest.fixture(scope="function")
def conn_with_data(postgres_container: PostgresContainer) -> str:
    engine = create_engine(postgres_container.get_connection_url())
    conn = engine.connect()

    create_table(conn)
    transactions = [
        Transaction(
            description="test_description 1",
            price=1,
            quantity=10,
            amount=0,
        ),
        Transaction(
            description="test_description 2",
            price=2,
            quantity=20,
            amount=0,
        ),
        Transaction(
            description="test_description 3",
            price=3,
            quantity=30,
            amount=0,
        ),
    ]
    for transaction in transactions:
        insert_transaction(conn, transaction)
    return postgres_container.get_connection_url()
