from django.db import models

# Create your models here.
class Report(models.Model):
	# nombre doctor
	# fecha consulta
	# nombre paciente
	# edo paciente
	# observaciones
	# sugerencias
	doc_name = models.CharField(max_length=100)
	patient_name = models.CharField(max_length=100)
	consult_date = models.CharField(max_length=50)
	patient_state = models.CharField(max_length=200)
	observ = models.CharField(max_length=500)
	suggest = models.CharField(max_length=500)
