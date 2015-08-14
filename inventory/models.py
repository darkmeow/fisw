# -*- coding: utf-8 -*-
 
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
		return u"{0}".format(self.name)

class SubLocation(models.Model):
	'''Model for the sublocation '''
	name = models.CharField(max_length=100)
	def __unicode__(self):
		return u"{0}".format(self.name)

class Item(models.Model):
	'''Model for the item's inventory '''
	ITEM_TYPE_CHOICES = (
		('Item', 'Item'),
		('Instrument', 'Instrument'),
		('Material', 'Material'),
		('Tool', 'Tool')
	)
	location = models.ForeignKey(Location)
	sublocation = models.ForeignKey(SubLocation)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	purchase_date = models.DateField()
	stock = models.IntegerField(default=1)
	item_type = models.CharField(max_length=10, choices=ITEM_TYPE_CHOICES, default='Item')
	photo = models.ImageField(upload_to="item_photo", blank=True, null=True)
	def __unicode__(self):
		return u"{0}".format(self.name)

	
class Client(models.Model):
	'''Model for the client of the inventory. '''
	user = models.OneToOneField(User)
	rut = models.CharField(max_length=15)
	loans = models.ManyToManyField(Item, through='Loan', blank=True)
	def __unicode__(self):
		return u"{0} | {1} {2}".format(self.user, self.user.first_name, self.user.last_name)



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
		return u"{0} - {1}".format(self.name, self.brief)


	
class Membership(models.Model):
	'''Link model for the many-to-many relationship
	of Projects and Clients that are members 
	'''
	client = models.ForeignKey(Client)
	project = models.ForeignKey(Project)
	date_joined = models.DateField()
	def __unicode__(self):
		return u"{0} en {1}".format(self.client, self.project)

class Loan(models.Model):
	'''Model for the user's loans.
	They are created with is_active True by default (debt)
	When they return the item, is_active should change to False,
	and return_date should be now
	'''
	client = models.ForeignKey(Client)
	item = models.ForeignKey(Item)
	loan_date = models.DateTimeField()
	return_date = models.DateTimeField(blank=True, null=True)
	is_active = models.BooleanField(default=True)
	def cancel(self):
		self.is_active = False
		self.return_date = timezone.now()
		self.save()
		return
	def set_date(self, date):
		self.loan_date = date
		self.save()
	def isActive(self):
		return self.is_active
	def __unicode__(self):
		return u"{0} | {1} | {2}".format(self.client, self.item, self.loan_date)

