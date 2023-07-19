from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100,unique=True, null=False, blank=False),
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100,unique=True, null=False, blank=False)
    author = models.ManyToManyField(Author, related_name='books'),
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title