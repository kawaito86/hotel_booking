from django.contrib import admin
from .models import Room, Booking, PricingRule

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(PricingRule)