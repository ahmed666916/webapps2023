# Generated by Django 4.2.1 on 2023-05-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_remove_transaction_recipient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gbp_to_usd_rate',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=10),
        ),
    ]
