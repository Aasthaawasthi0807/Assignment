from datetime import timezone
from django.db import models
from decimal import *

# Create your models here.
STATUS_CHOICES = (
        ('Fiction', 'Fiction'),
        ('Horror', 'Horror'),
        ('Fantasy', 'Fantasy'),
        ('Comic', 'Comic'),
        ('Historical', 'Historical'),
        ('Classics', 'Classics'),
    )

class Books(models.Model):
    book_name = models.CharField(max_length=250,default='')
    #email = models.EmailField(max_length=100)
    published_on = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    #phone_number = models.CharField( max_length=17, blank=True) 
    category = models.CharField(max_length=100, choices=STATUS_CHOICES,default=False)
    author = models.CharField(max_length=30,default='')
    price = models.DecimalField(max_digits=6, decimal_places=2,default =0.00)
    #public = models.BooleanField(default=True)