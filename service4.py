import time
from sql_queries import create_table, get_transactions
from credentials import conn

create_table(conn)

if __name__ == '__main__':
    while True:
        transactions = get_transactions(conn)
        print("-------------------- >>")
        for transaction in transactions:
            print(transaction)
        print("-------------------- <<")
        time.sleep(5)
