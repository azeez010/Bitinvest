# Generated by Django 4.1.1 on 2022-09-19 16:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biti', '0005_alter_kgs_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kgs',
            name='key',
            field=models.CharField(default=uuid.UUID('4a749ad0-bb1f-446f-b1a3-4417e9ddd4aa'), max_length=64),
        ),
    ]
