# Generated by Django 4.2.3 on 2023-07-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudProjet_api', '0005_alter_author_author_name_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(error_messages={'blank': "Le champ 'author_name' ne peut pas être vide."}, max_length=100, unique=True),
        ),
    ]
