from sqlalchemy.engine import Connection
from sqlalchemy import text

from transaction import Transaction


def create_table(conn: Connection):
    query = """
    CREATE TABLE IF NOT EXISTS transactions (
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        amount INTEGER,
        created DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'new'
        )
    """

    conn.execute(text(query))
    conn.commit()


def insert_transaction(conn: Connection, transaction: Transaction):
    query = """
    INSERT INTO transactions (description, price, quantity, amount)
    VALUES (:description, :price, :quantity, :amount);
    """

    conn.execute(
        text(query),
        parameters={
            "description": transaction.description,
            "price": transaction.price,
            "quantity": transaction.quantity,
            "amount": transaction.amount,
        },
    )
    conn.commit()


def update_transactions(conn: Connection):
    query = "UPDATE transactions SET amount=price*quantity, status='calculated' WHERE status='new';"
    conn.execute(text(query))
    conn.commit()


def complete_transactions(conn: Connection):
    query = "UPDATE transactions SET status='completed' WHERE status='calculated';"
    conn.execute(text(query))
    conn.commit()


def get_transactions(conn: Connection) -> list[Transaction]:
    query = "SELECT * FROM transactions;"
    print("ddd")
    transactions = conn.execute(text(query)).fetchall()
    print("ddd1")
    return [Transaction(
        id=transaction[0],
        description=transaction[1],
        price=transaction[2],
        quantity=transaction[3],
        amount=transaction[4],
        created=transaction[5],
        status=transaction[6],
    ) for transaction in transactions]
