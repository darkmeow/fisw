from django.contrib import admin
from inventory.models import Client, Administrator, Location, Item
# Register your models here.
<<<<<<< HEAD
from inventory.models import Item, Location, Client, Project, Loan, Administrator
from django.contrib import admin

admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Loan)
admin.site.register(Administrator)
=======

admin.site.register(Client)
admin.site.register(Administrator)
admin.site.register(Location)
admin.site.register(Item)
>>>>>>> 86e5b201daaef7535935ca5e514d9460c47afa4f
