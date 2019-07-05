from django.db import models
# Create your models here.
class RegistroTanques(models.Model):
	Id=models.AutoField(primary_key=True)
	Fecha=models.DateField()
	Sensor1=models.FloatField()
	Sensor2=models.FloatField()
	idLocal=models.IntegerField(null=True)
