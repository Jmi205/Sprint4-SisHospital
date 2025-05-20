from django.shortcuts import render
from .forms import EventoMedicoForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .logic.eventoMedico_logic import create_eventoMedico, get_eventosMedicos
from sisHospital.auth0backend import getRole
from django.conf import settings
import requests
import json


def eventosMedicos_list(request):
    eventosMedicos = get_eventosMedicos()
    context = {
        'eventosMedicos_list': eventosMedicos[:10]
    }
    return render(request, 'EventoMedico/eventoMedico.html', context)

def eventoMedico_create(request):
    role = getRole(request)
    if role in ['Supervisor', 'Medico']:
        if request.method == 'POST':
            form = EventoMedicoForm(request.POST)
            if form.is_valid():
                if check_paciente(form):
                    create_eventoMedico(form)
                    messages.add_message(request, messages.SUCCESS, 'EventoMedico create successful')
                    return HttpResponseRedirect(reverse('eventoMedicoCreate'))
                else:
                    return HttpResponse("unsuccessfully created eventoMedico. Paciente or ... does not exist")

            else:
                print(form.errors)
        else:
            form = EventoMedicoForm()

        context = {
            'form': form,
        }
        return render(request, 'EventoMedico/eventoMedicoCreate.html', context)

    else:
        return HttpResponse('Unauthorized User')


def check_paciente(form: EventoMedicoForm):
    r = requests.get(settings.PATH_PAC, headers={"Accept":"application/json"})
    pacientes = r.json()
    for paciente in pacientes:
        if form.cleaned_data["paciente"] == paciente["id"]:
            return True
    return False
