from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
	'''Model for the WCG Projects. '''
	name = models.CharField(max_length=100)
	manager = models.ForeignKey(Client)
	members = models.ManyToManyField(Client, through='Membership')
	start_date = models.DateTimeField('start date')
	is_active = models.BooleanField(default=True)

class Client(models.Model):
	'''Model for the client of the inventory. '''
	user = models.OneToOneField(User)

class Admin(models.Model):
	'''Model for the inventory administrator. '''
	user = models.OneToOneField(User) 
	
class Membership(models.Model):
	'''Link model for the many-to-many relationship
	of Projects and Clients that are members '''
	client = models.ForeignKey(Client)
	project = models.ForeignKey(Project)
	date_joined = models.DateField()
	
class Item(models.Model):
	'''Model for the item's inventory '''
	location = models.ForeignKey(Location)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	purchase_date = models.DateTimeField()
	
class Location(models.Model):
	'''Model for the location '''
	name = models.CharField(max_length=100)
	
class Instrument(models.Model):
	'''Model for the Instruments '''
	item = models.OneToOneField(Item)

class Material(models.Model):
	'''Model for the Instruments '''
	item = models.OneToOneField(Item)

	
class Tool(models.Model):
	'''Model for the Instruments '''
	item = models.OneToOneField(Item)


