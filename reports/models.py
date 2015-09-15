from django.db import models
from users.models import Doctor, Patient

# Create your models here.
class Report(models.Model):
	# nombre doctor
	# fecha consulta
	# nombre paciente
	# edo paciente
	# observaciones
	# sugerencias
	doc_name = models.CharField(max_length=100)
	# doctor = models.ForeignKey(Doctor)
	# patient = models.ForeignKey(Patient)
	patient_name = models.CharField(max_length=100)
	consult_date = models.CharField(max_length=50)
	report_type = models.CharField(max_length=15)
	observ = models.TextField()

class PsyReport(models.Model):
	report = models.OneToOneField(Report, primary_key=True)
	patient_state = models.CharField(max_length=200)
	suggest = models.TextField()


class NutReport(models.Model):
	report = models.OneToOneField(Report, primary_key=True)
	weight = models.FloatField()
	height = models.FloatField()
	pressure = models.TextField()
	glucosa = models.TextField()
	appetite = models.TextField()
	imc = models.TextField()
	suggest = models.TextField()