# Generated by Django 4.1.1 on 2022-09-19 18:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biti', '0006_alter_kgs_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kgs',
            name='key',
            field=models.CharField(default=uuid.UUID('8a341929-5747-4880-a83d-bdda20896d70'), max_length=64),
        ),
    ]