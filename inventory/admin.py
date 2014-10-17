from django.contrib import admin
from inventory.models import Client, Administrator, Location, Item
# Register your models here.

admin.site.register(Client)
admin.site.register(Administrator)
admin.site.register(Location)
admin.site.register(Item)