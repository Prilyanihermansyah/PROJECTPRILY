from django.contrib import admin
from django.urls import path
from KNK.views import index 
from PD.views import situs
from PDS.views import pds
from PH.views import ph 
from TAD.views import tad
from UD.views import ud
from UKK.views import ukk
from UP.views import up 
from PROFIL.views import profil
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('knk/', index),
    path('pd/', situs),
    path('pds/', pds),
    path('ph/', ph),
    path('tad/', tad),
    path('ud/', ud), 
    path('ukk/', ukk),
    path('up/', up),
    path('profil/', profil),
    path('', views.index),
    

]