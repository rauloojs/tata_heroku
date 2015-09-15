from django.db import models
from django.contrib.auth.models import User
from reports.models import *

# Modelos para la gestion de usuarios, cada profile corresponde a un tipo de usuario

class UserProfile(models.Model):
	# Registro como usuario
	user = models.ForeignKey(User, unique=True)

class Relative(UserProfile):

	push_key = models.TextField()
	
class Patient(models.Model):
	# Registro como paciente
	# user = models.ForeignKey(User, unique=True)

	age = models.IntegerField()
	suffers = models.TextField()
	relative = models.ManyToManyField(Relative)

class AdminUser(UserProfile):
	pass

class Doctor(UserProfile):

	speciality = models.TextField()