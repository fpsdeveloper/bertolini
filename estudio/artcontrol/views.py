from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'indice.html')

def casos(request):
    html = "<html><body>Listado Actual de Casos</body></html>"
    return HttpResponse(html)
