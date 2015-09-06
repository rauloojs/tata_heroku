from rest_framework import serializers
from api.models import Doctor, Patient, Tag

class DoctorSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse Doctor data
	"""

	class Meta:
		model = Doctor
		fields = ( 'doc_name', 'doc_esp', 'id' )

class PatientSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse Patient data
	"""

	class Meta:
		model = Patient
		fields = ( 'pat_name', 'id' )

class TagSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse Tag data
	"""

	class Meta:
		model = Tag
		fields = ( 'tag_name', 'id' )