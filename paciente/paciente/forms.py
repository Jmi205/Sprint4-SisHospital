from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre', 
            'apellido', 
            'tipoSangre',
            'alergias',
            'condicionesMedicas',
            'fechaNacimiento', 
            'historiaClinca'

        ]
        
        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'tipoSangre' : 'TipoSangre',
            'alergias' : 'Alergias',
            'condicionesMedicas' : 'CondicionesMedicas',
            'fechaNacimiento' : 'FechaNacimiento', 
            'historiaClinica' : 'historiaClinica'

        }