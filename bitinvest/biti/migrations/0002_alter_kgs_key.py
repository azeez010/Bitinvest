# Generated by Django 4.1.1 on 2022-09-18 23:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kgs',
            name='key',
            field=models.CharField(default=uuid.UUID('9ae6c65a-ec37-443c-a45d-38632e6cda46'), max_length=64),
        ),
    ]
