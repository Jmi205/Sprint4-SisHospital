from django import forms
from .models import EventoMedico

class EventoMedicoForm(forms.ModelForm):
    class Meta:
        model = EventoMedico
        fields = [
            'fechaEvento',
            'descripcion',
            'tipoEvento',
            'paciente',

        ]

        labels = {
            'fechaEvento':'FechaEvento',
            'descripcion':'Descripcion',
            'tipoEvento':'TipoEvento',
            'paciente':'Paciente',
        }
        

