# Generated by Django 4.1.1 on 2022-09-20 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_purchase_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='payment_successful',
            field=models.BooleanField(default=False),
        ),
    ]