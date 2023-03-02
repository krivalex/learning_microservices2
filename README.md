Task:
Create a new table: transactions, with the following columns:
- id (int, primary key)
- description (varchar)
- price (integer)
- quantity (integer)
- amount (integer)
- created (date) default now
- status (varchar) default "new"

Services: 
1. Create a new transaction every minute.
1. Read all transactions from the database and multiplies price by quantity and stores it in amount and change status to "calculated". 
1. Update all transactions with status "calculated" and change status to "updated".

Instructions:

Inserting goes like this:
```python
cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (type, description, amount) VALUES (%s, %s, %s)", (expense.type, 
expense.description, expense.amount))
conn.commit()
```
    
Selecting goes like this:
```python
cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    return [{
        "id": expense[0],
        "type": expense[1],
        "description": expense[2],
        "amount": expense[3],
        "created": expense[4]
    } for expense in expenses
    ]
```