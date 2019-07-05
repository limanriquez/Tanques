from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from tanques.serializers import *
from tanques.views import *
from urllib.request import urlopen
from tanques.models import *
import time

# Create your views here.
@login_required()
def tanques(request):
	context={
		"title":"Registro de tanques",
	}
	return render (request,"tanques.html", context)

class RegistroTanquesViewSet(viewsets.ModelViewSet):
	queryset=RegistroTanques.objects.all()
	serializer_class=RegistroTanquesSerializer
