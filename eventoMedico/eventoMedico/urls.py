from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('eventosMedicos/', views.eventosMedicos_list),
    path('eventoMedicoCreate/', csrf_exempt(views.eventoMedico_create), name='eventoMedicoCreate'),
]