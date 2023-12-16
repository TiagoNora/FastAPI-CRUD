from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str
    description: str
    designation: str
    company: str
    price: float
    created_at: Optional[datetime] = Field(default=datetime.utcnow(), nullable=False)
    last_edited: Optional[datetime] = Field(default_factory=datetime.utcnow, nullable=False)

class ProductCreate(SQLModel):
    sku: str
    description: str
    designation: str
    company: str
    price: float

class ProductRead(SQLModel):
    id: int
    sku: str
    description: str
    designation: str
    company: str
    price: float
    created_at: datetime
    last_edited: datetime