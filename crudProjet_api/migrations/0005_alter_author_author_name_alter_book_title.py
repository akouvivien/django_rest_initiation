# Generated by Django 4.2.3 on 2023-07-20 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudProjet_api', '0004_alter_author_author_name_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(error_messages={'blank': "Le champ 'author_name' ne peut pas être vide."}, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(error_messages={'blank': "Le champ 'title' ne peut pas être vide."}, max_length=100),
        ),
    ]
