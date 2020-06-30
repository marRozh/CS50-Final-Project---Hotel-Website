from django.contrib import admin

from .models import Apartment, Booking, Category, Bedtype, Guestnum
# Register your models here.
admin.site.register(Apartment)
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Bedtype)
admin.site.register(Guestnum)