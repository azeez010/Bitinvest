# Generated by Django 4.1.1 on 2022-09-19 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('biti', '0006_alter_kgs_key'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='invest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_invest', to='biti.invest'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='kgs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_kgs', to='biti.kgs'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='trade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_trade', to='biti.trade'),
        ),
    ]