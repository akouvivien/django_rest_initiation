from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=100,unique=True, null=False, blank=False),
    #par defaut la variable is_available est defini a true cette variable sera modifier a la suppression
    is_available = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_authors')
    created_at = models.DateTimeField(default=timezone.now)

    modified_at = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modified_authors')


    class Meta:
        # Définir l'ordre d'affichage par défaut (optionnel)
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100,unique=True, null=False, blank=False)
    author = models.ManyToManyField(Author, related_name='books'),
    #par defaut la variable is_available est defini a true cette variable sera modifier a la suppression
    is_available = models.BooleanField(default=True)
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_books')
    created_at = models.DateTimeField(default=timezone.now)

    modified_at = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modified_books')

    class Meta:
        # Définir l'ordre d'affichage par défaut (optionnel)
         ordering = ['-created_at']

    def __str__(self):
        return self.title