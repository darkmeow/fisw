from django.db import models
from django.contrib.auth.models import User
"""
class Project(models.Model):
	'''Model for the WCG Projects. '''
	name = models.CharField(max_length=100)
	manager = models.ForeignKey(Client)
	start_date = models.DateTimeField('start date')

class Client(models.Model):
	'''Model for the client of the inventory. '''
	user = models.OneToOneField(User)

class Admin(models.Model):
	'''Model for the inventory administrator. '''
	user = models.OneToOneField(User) 
"""
