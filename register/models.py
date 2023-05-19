from django.db import models


# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    CURRENCY_CHOICES = (
        ('GBP', 'British Pound'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    gbp_to_usd_rate = models.DecimalField(max_digits=10, decimal_places=4, default=0.0)

    def __str__(self):
        return self.username


