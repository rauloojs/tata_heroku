from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView )

from api.models import Doctor, Patient, Tag
from api.serializers import DoctorSerializer, PatientSerializer, TagSerializer
from django.http import HttpResponse, HttpResponseForbidden

# Example using function based views
# -----------------------------------

# @api_view(['GET', 'POST'])
# def task_list(request):
#     """
#     List all task, or create a new one
#     """

#     # GET Request
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks)
#         return Response(serializer.data)

#     # POST Request
#     if request.method == 'POST':
#         serializer = TaskSerializer(data=request.DATA)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST
#             )


# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail(request, pk):
#     """
#     Get, update, or delete a specific task
#     """
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     # GET request
#     if request.method == 'GET':
#         serializer = TaskSerializer( task )
#         return Response( serializer.data )

#     # PUT request
#     if request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.DATA)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)

#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST
#             )

#     # DELETE request
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# Example using class based views
# -----------------------------------
def search_doc(request):
 
    #if not request.POST.__contains__('term'):
     #   return HttpResponseForbidden("")
 
    # Hacemos la consulta para aquellos elementos que empiecen por start ordenados por nombre
    term = request.GET.get('term', '')
    query = Doctor.objects.filter(doc_name__icontains=term).order_by('doc_name')
 
    # Serializamos
    objects = u'['
    
    for i in query:
        objects += u'"%s",\n' % (i.doc_name.replace('"',''))
    
    objects = objects.strip(",\n");
    objects += u']'
 
    return HttpResponse(objects, content_type="text/plain")

def search_pat(request):
 
    #if not request.POST.__contains__('term'):
     #   return HttpResponseForbidden("")
 
    # Hacemos la consulta para aquellos elementos que empiecen por start ordenados por nombre
    term = request.GET.get('term', '')
    query = Patient.objects.filter(pat_name__icontains=term).order_by('pat_name')
 
    # Serializamos
    objects = u'['
    
    for i in query:
        objects += u'"%s",\n' % (i.pat_name.replace('"',''))
    
    objects = objects.strip(",\n");
    objects += u']'
 
    return HttpResponse(objects, content_type="text/plain")

def search_tag(request):
 
    #if not request.POST.__contains__('term'):
     #   return HttpResponseForbidden("")
 
    # Hacemos la consulta para aquellos elementos que empiecen por start ordenados por nombre
    term = request.GET.get('term', '')
    query = Tag.objects.filter(tag_name__icontains=term).order_by('tag_name')
 
    # Serializamos
    objects = u'['
    
    for i in query:
        objects += u'"%s",\n' % (i.tag_name.replace('"',''))
    
    objects = objects.strip(",\n");
    objects += u']'
 
    return HttpResponse(objects, content_type="text/plain")

class DoctorMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorList(DoctorMixin, ListCreateAPIView):
    """
    Return a list of all the Doctors, or
    create new ones
    """
    pass

class DoctorDetail(DoctorMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific Doctor, update it, or delete it.
    """
    pass


class PatientMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientList(PatientMixin, ListCreateAPIView):
    """
    Return a list of all the Patients, or
    create new ones
    """
    pass

class PatientDetail(PatientMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific Patient, update it, or delete it.
    """
    pass


class TagMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagList(TagMixin, ListCreateAPIView):
    """
    Return a list of all the Tags, or
    create new ones
    """
    pass

class TagDetail(TagMixin, RetrieveUpdateDestroyAPIView):
    """
    Return a specific Tag, update it, or delete it.
    """
    pass