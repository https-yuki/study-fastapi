from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"

class ItemCreate(BaseModel):
    name: str = Field(min_length = 2, max_length = 20, examples = ["PC"])
    price: int = Field(gt = 0, examples = [10000])
    description: Optional[str] = Field(None, examples = ["美品です"])

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length = 2, max_length = 20, examples = ["PC"])
    price: Optional[int] = Field(None, gt = 0, examples = [10000])
    description: Optional[str] = Field(None, examples = ["美品です"])
    status: Optional[ItemStatus] = Field(None, examples = [ItemStatus.SOLD_OUT])

class ItemResponse(BaseModel):
    id: int = Field(gt = 0, examples = [1])
    name: str = Field(min_length = 2, max_length = 20, examples = ["PC"])
    price: int = Field(gt = 0, examples = [10000])
    description: Optional[str] = Field(None, examples = ["美品です"])
    status: ItemStatus = Field(examples = [ItemStatus.ON_SALE])
    created_at: datetime
    updated_at: datetime
    user_id: int

    model_config = ConfigDict(from_attributes = True)

class UserCreate(BaseModel):
    username: str = Field(min_length = 2, examples = ["user1"])
    password: str = Field(min_length = 8, examples = ["test1234"])

class UserResponse(BaseModel):
    id: int = Field(gt = 0, examples = [1])
    username: str = Field(min_length = 2, examples = ["user1"])
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes = True)

class Token(BaseModel):
    access_token: str
    token_type: str

class DecodedToken(BaseModel):
    username: str
    user_id: int