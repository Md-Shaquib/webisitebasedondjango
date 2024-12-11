from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #when using charfield max length is mandatory
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000,null=False,blank=False,default=0.00)
    summary = models.TextField(default="Hello")
    featured = models.BooleanField(default=True)
