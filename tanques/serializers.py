from rest_framework import serializers
from tanques.models import *

class RegistroTanquesSerializer(serializers.ModelSerializer):
	class Meta:
		model=RegistroTanques
		exclude=[]