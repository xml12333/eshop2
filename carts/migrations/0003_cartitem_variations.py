# Generated by Django 3.2.13 on 2022-04-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220417_1551'),
        ('carts', '0002_rename_card_id_cart_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]