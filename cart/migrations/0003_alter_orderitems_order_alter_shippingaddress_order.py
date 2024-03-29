# Generated by Django 4.0.3 on 2022-04-20 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_createdat_alter_order_deliveredat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderitems', to='cart.order'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping', to='cart.order'),
        ),
    ]
