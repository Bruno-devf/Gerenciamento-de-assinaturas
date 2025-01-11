from sqlmodel import Field, SQLModel, create_engine, Relationship
from typing import Optional
from datetime import date
from decimal import Decimal

class Subscribers(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal
    
payments: list["Payment"] = Relationship(back_populates="subscriber")

class Payment(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscriber_id: int = Field(foreign_key="subscribers.id")
    subscriber: Subscribers = Relationship()
    date: date