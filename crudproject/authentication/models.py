from datetime import timezone
import datetime
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
    category = models.CharField(max_length=100, choices=STATUS_CHOICES,default=False)
    author = models.CharField(max_length=30,default='')
    price = models.DecimalField(max_digits=6, decimal_places=2,default =0.00)
    