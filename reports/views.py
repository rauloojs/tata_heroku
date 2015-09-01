# encoding: utf8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from reports.models import Report

import json
import requests
import sys


# Create your views here.
def index(request):
	return render(request, 'reports/index.html')

def send(request):
	# make request
	# nombre doctor
	# fecha consulta
	# nombre paciente
	# edo paciente
	# observaciones
	# sugerencias
	doc_name = request.POST.get('nombre_dr', "")
	patient_name = request.POST.get('nombre_pac', "")
	consult_date = request.POST.get('fecha', "")
	patient_state = request.POST.get('estado_pac', "")
	observ = request.POST.get('comentarios', "")
	suggest = request.POST.get('sugerencias', "")

	rep = Report(doc_name=doc_name, patient_name=patient_name, consult_date=consult_date, patient_state=patient_state, observ=observ, suggest=suggest)
	rep.save()

	url = 'https://android.googleapis.com/gcm/send'
	headers = {'Content-Type': 'application/json',
				'Authorization': 'key=AIzaSyCH7B7qMMbLnQdj6WG1yuvPp3SlsLHtBds'}
	payload = {
	          "data": {
	            "fecha": consult_date,
	            "doctor": doc_name,
	            "paciente": patient_name,
	            "observaciones": observ,
	            "sugerencias": suggest
	          },
	          "registration_ids": [
	            "APA91bHDXfzISMoo6OfqhhODnU7TeNzqCxeE7lYZHhdI801wazh1e7vbITZVTqwKU5avNW0myInlZW3Aat3S8gzqawN9G5fQEkMVNvqkDHRRYt1IDsFrPuc"
	          ]
	}

	try:
		r = requests.post(url, data=json.dumps(payload))
		#r = requests.post(url, headers=headers, data=json.dumps(payload))
	except requests.exceptions.ConnectionError:
		return render(request, 'reports/index.html', {
            'error_message': "No hay conexión a internet, intente más tarde",
        })
	else:
		print >>sys.stderr, "POST request response: ", r.status_code
		if r.status_code == 200:
			code = 0
		else:
			code = 1
		#print >>sys.stderr, consult_date
		return HttpResponseRedirect(reverse('reports:results', args=(rep.id, code)))
	finally:
		pass


def results(request, rep_id, status):
	# return render(request, 'reports/results.html')
	r = get_object_or_404(Report, pk=rep_id)
	return render_to_response('reports/results.html', {'report': r, 'status': status})