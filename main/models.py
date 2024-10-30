from django.db import models

class purchase(models.Model):

    network_choice = (
        ('mtn', "MTN"),
        ('airtel', "AIRTEL"),
        ('9mobile', "9MOBILE"),
        ('glo', "GLO"),
    )

    phone_number = models.CharField(max_length=14)
    mobile_network = models.CharField(choices=network_choice, max_length=10)
    message = models.CharField(max_length=200)
    ref_code = models.CharField(unique=True,  max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
