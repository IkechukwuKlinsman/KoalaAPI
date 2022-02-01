from pickle import TRUE
from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add= True)
    date_created = models.DateTimeField(auto_now= True)