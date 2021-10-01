from django.db import models

# Create your models here.

class CompletedQuote(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    tweet = models.CharField(max_length=240)
    font = models.CharField(max_length=100)
    picture_url = models.CharField(max_length=2048)