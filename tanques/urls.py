from django.conf.urls import url, include 
from tanques.views import * 
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.contrib.auth.views import login

router=DefaultRouter()
router.register(r'RegistroTanques',RegistroTanquesViewSet)
RegistroTanquesViewSet
urlpatterns=[
	url(r'^api/v1/', include(router.urls)),
	url(r'tanques$', tanques, name='tanques'),
]
