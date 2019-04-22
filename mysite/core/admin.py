from django.contrib import admin
from .models import Tickets, AddPrice, AddMovie
# Register your models here.

@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display=['id','user_name','seat_count','seat_numbers','total_amount','date_time']
    list_filter=['id','user_name','seat_count','seat_numbers','total_amount','date_time']

@admin.register(AddPrice)
class AddPriceAdmin(admin.ModelAdmin):
    list_display=['price']
    list_filter=['price']
@admin.register(AddMovie)
class AddMovieAdmin(admin.ModelAdmin):
    list_display=['movie_name','movie_image','movie_date']
    list_filter=['movie_name','movie_image','movie_date']


