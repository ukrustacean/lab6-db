
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DataCreate(BaseModel):
    id: Optional[int] = None
    name: str
    content: str
    upload_date: Optional[datetime] = None
    last_edit_date: Optional[datetime] = None
    category_id: int


class CategoryCreate(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None


class DataResponse(DataCreate):
    class Config:
        orm_mode = True


class CategoryResponse(CategoryCreate):
    class Config:
        orm_mode = True


class CategoryPatch(BaseModel):
    id: int = None
    name: str = None
    description: Optional[str] = None


class DataPatch(BaseModel):
    id: int = None
    name: str = None
    content: str = None
    upload_date: datetime = None
    last_edit_date: Optional[datetime] = None
    category_id: int = None

