# Generated by Django 4.1.1 on 2022-09-20 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biti', '0010_rename_end_invest_end_range_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investmentcountries',
            options={'verbose_name': 'investment Country', 'verbose_name_plural': 'investment Countries'},
        ),
        migrations.AlterModelOptions(
            name='kgs',
            options={'verbose_name': 'KGS', 'verbose_name_plural': 'KGS'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Setting', 'verbose_name_plural': 'Settings'},
        ),
        migrations.AlterField(
            model_name='invest',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='kgs',
            name='key',
            field=models.CharField(default=uuid.UUID('5d5c3c12-9c41-4b3d-b9d7-7e2ca3572342'), max_length=64),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_partner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
