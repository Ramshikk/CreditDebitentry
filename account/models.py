from django.db import models

# Create your models here.
class Entry(models.Model):
    date = models.DateField()
    particulars = models.CharField(max_length=255)
    transaction_type = models.IntegerField()  
    amount = models.DecimalField(max_digits=10, decimal_places=2)
