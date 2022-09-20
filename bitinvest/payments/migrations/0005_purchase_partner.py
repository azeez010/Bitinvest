# Generated by Django 4.1.1 on 2022-09-20 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biti', '0012_alter_kgs_key'),
        ('payments', '0004_rename_product_purchase_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_partner', to='biti.partner'),
        ),
    ]
