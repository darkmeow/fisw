from django.contrib import admin
from inventory.models import Client, Administrator, Location, Item, Loan, Project
# Register your models here.
admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Loan)
admin.site.register(Administrator)

