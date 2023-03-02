from dataclasses import dataclass
from typing import Optional


@dataclass
class Transaction:
    description: str
    price: int
    quantity: int
    amount: int
    created: str = ""
    status: str = "new"
    id: Optional[int] = None
