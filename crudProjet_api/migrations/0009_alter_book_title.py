# Generated by Django 4.2.3 on 2023-07-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudProjet_api', '0008_alter_author_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(error_messages={'blank': "Le champ 'title' ne peut pas être vide."}, max_length=100, unique=True),
        ),
    ]