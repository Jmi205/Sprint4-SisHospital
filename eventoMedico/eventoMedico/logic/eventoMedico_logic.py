from ..models import EventoMedico

def get_eventosMedicos():
    queryset = EventoMedico.objects.all()
    return (queryset)

def create_eventoMedico(form):
    eventoMedico = form.save()
    eventoMedico.save()
    return ()