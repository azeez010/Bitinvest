# Generated by Django 4.1.1 on 2022-09-18 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('biti', '0002_alter_kgs_key'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('Kgs', 'KGS'), ('Trade', 'TRADE'), ('Invest', 'INVEST'), ('Partner', 'PARTNER')], max_length=50)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_buyer', to=settings.AUTH_USER_MODEL)),
                ('invest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_invest', to='biti.invest')),
                ('kgs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_kgs', to='biti.kgs')),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_trade', to='biti.trade')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(-1, 'Not Started'), (0, 'Unconfirmed'), (1, 'Partially Confirmed'), (2, 'Confirmed')], default=-1)),
                ('order_id', models.CharField(max_length=250)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('btcvalue', models.IntegerField(blank=True, null=True)),
                ('received', models.IntegerField(blank=True, null=True)),
                ('txid', models.CharField(blank=True, max_length=250, null=True)),
                ('rbf', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_invoice', to='payments.purchase')),
            ],
        ),
    ]