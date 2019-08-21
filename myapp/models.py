from django.db import models


# Create your models here.
class Sale(models.Model):
    product_id = models.IntegerField
    destination_id = models.IntegerField

    client_name = models.CharField(max_length=200)
    client_email = models.EmailField
    boarding = models.DateField('boarding date')
    landing = models.DateField('landing date')

    net_price = models.FloatField
    elder_net_price = models.FloatField

    created_at = models.DateTimeField

