from django.db import models
from datetime import datetime

class Guest(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254)
    message = models.TextField()
    submission_date = models.DateTimeField(default=datetime.now, blank=True)

# Create your models here.
