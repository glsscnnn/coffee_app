from django.db import models

# order table this is like a spreadsheet
class Order(models.Model):
   bean = models.CharField(max_length=200)
   address = models.CharField(max_length=200)
   name = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')