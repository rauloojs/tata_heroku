# encoding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from reports.models import Report, PsyReport, NutReport
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

import json
import requests
import sys
import datetime
import time

# Create your views here.
@login_required
def index(request, username):
	return render_to_response('reports/index.html', {'user': request.user})

@login_required
def psychological(request, username):
	return render_to_response('reports/psychological.html', {'user': request.user, 'v_date': datetime.datetime.now()}, context_instance=RequestContext(request))

@login_required
def nutritional(request, username):
	return render_to_response('reports/nutritional.html', {'user': request.user, 'v_date': datetime.datetime.now()}, context_instance=RequestContext(request))

@login_required
def physiotherapy(request, username):
	return render_to_response('reports/physiotherapy.html', {'user': request.user, 'v_date': datetime.datetime.now()}, context_instance=RequestContext(request))

@login_required
def geriatric(request, username):
	return render_to_response('reports/geriatric.html', {'user': request.user, 'v_date': datetime.datetime.now()}, context_instance=RequestContext(request))

@login_required
def send(request):

	# Obtenemos los campos comunes entre reportes
	report_type = request.POST.get('form_type', "")
	doc_name = request.POST.get('nombre_dr', "")
	patient_name = request.POST.get('nombre_pac', "")
	consult_date = request.POST.get('fecha', "")
	observ = request.POST.get('observaciones', "")

	# Variables comunes
	url = 'https://android.googleapis.com/gcm/send'
	headers = {'Content-Type': 'application/json',
					'Authorization': 'key=AIzaSyCH7B7qMMbLnQdj6WG1yuvPp3SlsLHtBds'}

	# Creamos un objeto del tipo reporte del que heredará la info el reporte específico
	rep = Report(doc_name=doc_name, patient_name=patient_name, consult_date=consult_date, report_type=report_type, observ=observ)
	rep.save()

	if report_type == "psicologico":

		# Obtenemos campos únicos de reporte psicologico
		patient_state = request.POST.get('estado_pac', "")
		suggest = request.POST.get('sugerencias', "")

		psy = PsyReport(report=rep, patient_state=patient_state, suggest=suggest)
		psy.save()

		print >>sys.stderr, psy.report
		# Payload del reporte psicologico
		payload = {
		          "data": {
		          	"id": psy.report.id,
		          	"tipo": report_type,
		            "fecha": consult_date,
		            "timestamp": time.time(),
		            "doctor": doc_name,
		            "paciente": patient_name,
		            "observaciones": observ,
		            "sugerencias": suggest
		          },
		          "registration_ids": [
		            "APA91bHDXfzISMoo6OfqhhODnU7TeNzqCxeE7lYZHhdI801wazh1e7vbITZVTqwKU5avNW0myInlZW3Aat3S8gzqawN9G5fQEkMVNvqkDHRRYt1IDsFrPuc"
		          ]
		}
	elif report_type == "nutricional":

		# Obtenemos campos únicos de reporte nutricional
		weight = request.POST.get('peso', "")
		height = request.POST.get('talla', "")
		pressure = request.POST.get('presion', "")
		
		imc = request.POST.get('masa', "")
		glucosa = request.POST.get('glucosa', "")
		suggest = request.POST.get('sugerencias', "")
		
		appetite = request.POST.get('est_apetito', "")

		nut = NutReport(report=rep, weight=weight, height=height, pressure=pressure, imc=imc, glucosa=glucosa, suggest=suggest, appetite=appetite)
		nut.save()

		# Payload del reporte psicologico
		payload = {
		          "data": {
		          	"id": nut.report.id,
		          	"tipo": report_type,
		            "fecha": consult_date,
		            "timestamp": time.time(),
		            "doctor": doc_name,
		            "paciente": patient_name,
		            "observaciones": observ,
		            "peso": weight,
		            "talla": height,
		            "presion": pressure,
		            "imc": imc,
		            "glucosa": glucosa,
		            "sugerencias": suggest,
		            "est_apetito": appetite,
		          },
		          "registration_ids": [
		            "APA91bHDXfzISMoo6OfqhhODnU7TeNzqCxeE7lYZHhdI801wazh1e7vbITZVTqwKU5avNW0myInlZW3Aat3S8gzqawN9G5fQEkMVNvqkDHRRYt1IDsFrPuc"
		          ]
		}
	# El envío de la notificación es común para los reportes
	try:
		#r = requests.post(url, data=json.dumps(payload))
		r = requests.post(url, headers=headers, data=json.dumps(payload))
	except requests.exceptions.ConnectionError:
		if report_type == "psicologico":
			return render(request, 'reports/psychological.html', {
				'error_message': "No hay conexión a internet, intente más tarde",
			})
		elif report_type == "nutricional":
			return render(request, 'reports/nutritional.html', {
				'error_message': "No hay conexión a internet, intente más tarde",
			})
	else:
		print >>sys.stderr, "POST request response: ", r.status_code
		if r.status_code == 200:
			code = 0
		else:
			code = 1

		return HttpResponseRedirect(reverse('reports:results', args=(rep.id, code)))

		pass
	

@login_required
def results(request, rep_id, status):
	# return render(request, 'reports/results.html')
	
	r = get_object_or_404(Report, pk=rep_id)
	report_type = r.report_type

	if report_type == "psicologico":
		r = get_object_or_404(PsyReport, pk=r.id)
		return render_to_response('reports/psyresult.html', {'report': r, 'status': status, 'user': request.user}, context_instance=RequestContext(request))
	elif report_type == "nutricional":
		r = get_object_or_404(NutReport, pk=r.id)
		return render_to_response('reports/nutresult.html', {'report': r, 'status': status, 'user': request.user}, context_instance=RequestContext(request))
	elif report_type == "fisioterapia":
		r = get_object_or_404(FisReport, pk=r.id)
		return render_to_response('reports/fisresult.html', {'report': r, 'status': status, 'user': request.user}, context_instance=RequestContext(request))
	elif report_type == "geriatric":
		r = get_object_or_404(GerReport, pk=r.id)
		return render_to_response('reports/gerresult.html', {'report': r, 'status': status, 'user': request.user}, context_instance=RequestContext(request))