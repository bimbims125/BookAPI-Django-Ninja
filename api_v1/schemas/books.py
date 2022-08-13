from unicodedata import category
from ninja import Schema, ModelSchema
from api_v1.models import Book



class CategoryList(Schema):
    id: int
    name: str
    desc: str


class BookSchema(ModelSchema):
    category: CategoryList

    class Config:
        model = Book
        model_fields = '__all__'


class BookByCategorySchema(ModelSchema):
    category:CategoryList
    class Config:
        model = Book
        model_fields = '__all__'

class UpdateBookSchema(ModelSchema):
    class Config:
        model = Book
        model_exclude = ['id']
