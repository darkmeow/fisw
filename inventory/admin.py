from django.contrib import admin

# Register your models here.
from inventory.models import Item, Location, Client, Project, Loan, Administrator
from django.contrib import admin

admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Loan)
admin.site.register(Administrator)