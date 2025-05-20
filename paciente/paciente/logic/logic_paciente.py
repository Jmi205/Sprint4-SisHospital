from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    print(queryset)
    return (queryset)

def create_paciente(form):
    paciente = form.save()
    paciente.save()
    return ()
