from __future__ import unicode_literals

from django.db import models
import qrcode
from io import StringIO
# Create your models here.
class Tickets(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.TextField(max_length=100, null=True)
    seat_count = models.TextField(max_length=100, null=True)
    seat_numbers = models.TextField(max_length=100, null=True)
    total_amount = models.TextField(max_length=100, null=True)
    date_time = models.DateTimeField(auto_now=True)





    def __str__(self):
       return "{},{},{},{},{},{}".format(self.id,self.user_name,self.seat_count,self.seat_numbers,self.total_amount,self.date_time)
class AddMovie(models.Model):
    movie_name = models.CharField(max_length=100, null=True)
    movie_image = models.ImageField()
    movie_date = models.DateField()
    
    def __str__(self):
       return "{},{},{}".format(self.movie_name,self.movie_image,self.movie_date)
class AddPrice(models.Model):
    price = models.IntegerField(primary_key=True)
    def __str__(self):
       return "{}".format(self.price)