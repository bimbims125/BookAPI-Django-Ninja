import asyncio
from ..models import Book, Category
from ..schemas.books import BookSchema, BookByCategorySchema, UpdateBookSchema
from ..schemas.category import CategorySchema, UpdateCategorySchema
from ..error.error import BadRequest

from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist

from ninja import NinjaAPI
from typing import List

app = NinjaAPI(title='Book API', version=0.1)


@app.get('/book', response=List[BookSchema], tags=['Get'])
async def retrieveAllBook(request):
    if Category.DoesNotExist:
        raise BadRequest(
            'Cannot retrieve Book, there is a Book that has an invalid category')

    await asyncio.sleep(2)
    return await Book.objects.async_all()


@app.get('/book/{id}', response=BookSchema, tags=['Get'])
async def retrieveBookById(request, id: int):
    if Category.DoesNotExist:
        raise BadRequest(
            'Cannot retrieve Book, there is a Book that has an invalid category')
    try:
        _book = await Book.objects.async_get(id=id)
        await asyncio.sleep(2)
        return _book
    except Book.DoesNotExist as e:
        raise BadRequest(f"Book with id {id} doesn't exist") from e


@app.post('/book', tags=['Post'])
async def postBook(request, title: str, author: str, category: int):
    _book = await Book.objects.async_create(title=title, author=author, category_id=category)
    _book.save()
    await asyncio.sleep(2)
    return {
        'success': True,
        'status_code': 200,
        'message': 'Data has been created.'
    }


@app.get('/book/category/{id}', response=List[BookByCategorySchema], tags=['Get'])
async def retrieverBookByCategory(request, id: int):
    if Category.DoesNotExist:
        raise BadRequest(f"The Book with category_id {id} doesn't exist")

    await asyncio.sleep(2)
    return await Book.objects.async_filter(category_id=id)

@app.put('/book/{id}', tags=['Put'])
async def putBook(request, id: int, payload: UpdateBookSchema):
    try:
        _book = await Book.objects.async_get(id=id)
        _book.title = payload.title
        _book.author = payload.author
        _book.category_id = payload.category
        _book.save()
        await asyncio.sleep(2)
        return {
            'success': True,
            'status_code': 200,
            'message': 'Data has been updated'
        }
    except Book.DoesNotExist as e:
        raise BadRequest(f"Book with id {id} doesn't exist") from e


@app.delete('/book/{id}', tags=['Delete'])
async def deleteBook(request, id: int):
    try:
        _book = await Book.objects.async_get(id=id)
        _book.delete()
        await asyncio.sleep(2)
        return {
            'success': True,
            'status_code': 200,
            'message': f'Data with id {id} has been deleted.'
        }
    except Book.DoesNotExist as e:
        raise BadRequest(f"Book with id {id} doesn't exist") from e


@app.get('/category', response=List[CategorySchema], tags=['Get'])
async def retrieveCategory(request):
    await asyncio.sleep(2)
    return await Category.objects.async_all()


@app.get('/category/{id}',  response=CategorySchema, tags=['Get'])
async def retrieveCategoryById(request, id: int):
    try:
        _category = await Category.objects.async_get(id=id)
        await asyncio.sleep(2)
        return _category

    except Category.DoesNotExist as e:
        raise BadRequest(f"Category with id {id} doesn't exist") from e


@app.post('/category', tags=['Post'])
async def postCategory(request, name: str, desc: str):
    _category = await Category.objects.async_create(name=name, desc=desc)
    _category.save()
    await asyncio.sleep(2)
    return {
        'success': True,
        'status_code': 200,
        'message': 'Data has been created.'
    }


@app.put('/category/{id}', tags=['Put'])
async def updateCategory(request, id: int, payload: UpdateCategorySchema):
    try:
        _category = await Category.objects.async_get(id=id)
        _category.name = payload.name
        _category.desc = payload.desc
        _category.save()
        await asyncio.sleep(2)
        return {
            'success': True,
            'status_code': 200,
            'message': f"Data within id {id} has been updated"
        }
    except Category.DoesNotExist as e:
        raise BadRequest(f"Category with id {id} doesn't exist") from e


@app.delete('/category/{id}', tags=['Delete'])
async def deleteCategory(request, id: int):

    try:
        _category = await Category.objects.async_get(id=id)
        _category.delete()
        await asyncio.sleep(2)
        return {
            'success': True,
            'status_code': 200,
            'message': f"Data within id {id} has been deleted."
        }
    except Category.DoesNotExist as e:
        raise BadRequest(f"Category with id {id} doesn't exist") from e
