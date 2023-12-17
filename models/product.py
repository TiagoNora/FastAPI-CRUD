from sqlmodel import Field, SQLModel, Column
from typing import Optional
from datetime import datetime

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str
    description: str
    designation: str
    company: str
    price: float
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: Optional[datetime] = Field(sa_column=Column(onupdate=datetime.utcnow))

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
    updated_at: Optional[datetime]


class ProductUpdate(SQLModel):
    description: Optional[str]
    designation: Optional[str]
    company: Optional[str]
    price: Optional[float]