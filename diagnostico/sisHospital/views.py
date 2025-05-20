from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def healthCheck(request):
    return HttpResponse('Ok')
