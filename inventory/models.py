# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Administrator(models.Model):
	'''Model for the inventory administrator. '''
	user = models.OneToOneField(User) 
	def __unicode__(self):
		return u"{0} | {1} {2}".format(self.user, self.user.first_name, self.user.last_name)
	
class Location(models.Model):
	'''Model for the location '''
	administrator = models.ForeignKey(Administrator)
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	def __unicode__(self):
		return "{0}".format(self.name)

class Item(models.Model):
	'''Model for the item's inventory '''
	location = models.ForeignKey(Location)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	purchase_date = models.DateTimeField()
	count = models.IntegerField(default=1)
	def __unicode__(self):
		return "{0}".format(self.name)

	
class Client(models.Model):
	'''Model for the client of the inventory. '''
	user = models.OneToOneField(User)
	rut = models.CharField(max_length=15)
	loans = models.ManyToManyField(Item, through='Loan', blank=True)
	def __unicode__(self):
		return "{0} | {1} {2}".format(self.user, self.user.first_name, self.user.last_name)



class Project(models.Model):
	'''Model for the WCG Projects. '''
	manager = models.ForeignKey(Client)
	members = models.ManyToManyField(Client, through='Membership',related_name="%(app_label)s_%(class)s_related")
	name = models.CharField(max_length=100)
	brief = models.CharField(max_length=100)
	description = models.TextField()
	start_date = models.DateTimeField('start date')
	is_active = models.BooleanField(default=True)
	def __unicode__(self):
		return "{0} - {1}".format(self.name, self.brief)


	
class Membership(models.Model):
	'''Link model for the many-to-many relationship
	of Projects and Clients that are members 
	'''
	client = models.ForeignKey(Client)
	project = models.ForeignKey(Project)
	date_joined = models.DateField()
	def __unicode__(self):
		return "%s en %s".format(self.client, self.project)

class Instrument(Item):
	'''Model for the Instruments '''
	pass

class Material(Item):
	'''Model for the Instruments '''
	pass
	
class Tool(Item):
	'''Model for the Instruments '''
	pass

class Loan(models.Model):
	'''Model for the user's loans.
	They are created with is_active True by default (debt)
	When they return the item, is_active should change to False,
	and return_date should be now
	'''
	client = models.ForeignKey(Client)
	item = models.ForeignKey(Item)
	loan_date = models.DateTimeField(auto_now = True)
	return_date = models.DateTimeField(blank=True, null=True)
	is_active = models.BooleanField(default=True)
	def __unicode__(self):
		return "{0} | {1} | {2}".format(self.client, self.item, self.loan_date)

