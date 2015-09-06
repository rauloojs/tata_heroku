from django.db import models

# Create your models here.
class Doctor(models.Model):
	doc_name = models.CharField(max_length=100)
	doc_esp = models.CharField(max_length=100)

class Patient(models.Model):
	pat_name = models.CharField(max_length=100)

class Tag(models.Model):
	tag_name = models.CharField(max_length=50)