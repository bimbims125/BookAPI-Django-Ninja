from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=55, blank=False)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=55, blank=False)
    author = models.CharField(max_length=55)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, db_constraint=False)

    def __str__(self) -> str:
        return self.title
