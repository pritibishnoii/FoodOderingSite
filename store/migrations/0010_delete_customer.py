# Generated by Django 4.0 on 2022-02-14 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_rename_customer1_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]