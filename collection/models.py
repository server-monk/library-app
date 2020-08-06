import uuid

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Category(models.Model):
    genre_name = models.CharField(max_length=100)


class Publisher(models.Model):
    publisher = models.CharField(max_length=100)
    publisher_email = models.EmailField(unique=True)
    publisher_phone = PhoneNumberField(blank=True, null=True, help_text='Use the format: +(country) eg +2347000000123')


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField(unique=True)
    author_phone = PhoneNumberField(blank=True, null=True, help_text='Use the format: +(country) eg +2347000000123')


class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    genre = models.ForeignKey(Category, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=25)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publish_year = models.DateField()
    edition = models.CharField(max_length=100)
    book_format = models.CharField(max_length=100)
    is_available = models.BooleanField()
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book_title} {self.author}'
