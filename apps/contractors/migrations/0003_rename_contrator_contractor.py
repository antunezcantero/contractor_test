# Generated by Django 4.2 on 2023-04-26 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0002_alter_contrator_country'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contrator',
            new_name='Contractor',
        ),
    ]
