# Generated by Django 3.0.5 on 2020-04-14 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200414_0333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_author',
            new_name='author',
        ),
    ]
