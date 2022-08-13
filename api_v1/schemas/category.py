from pydantic import BaseModel
from ninja import ModelSchema, Schema

from api_v1.models import Category
from typing import Union


class BaseResponseModel(BaseModel):
    data: Union[dict, list] = None
    meta: dict = {}
    success: bool = True
    code: int = 200
    message: str = 'Success'


class BookList(Schema):
    id: int
    title: str
    author: str


class CategorySchema(ModelSchema):
    class Config:
        model = Category
        model_fields = '__all__'


class UpdateCategorySchema(ModelSchema):
    class Config:
        model = Category
        model_exclude = ['id']
