from django.db import models

# Create your models here.

class CompletedQuote(models.Model):


    id = models.CharField(max_length=100, primary_key=True)
    quote = models.CharField(max_length=1000)
    font_family = models.CharField(max_length=100)
    font_weight = models.CharField(max_length=50)
    font_style = models.CharField(max_length=50)
    picture_url = models.CharField(max_length=200)
    
  