from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from models import caso

def index(request):
    return render(request,'indice.html')

#Listado Original de Casos
def casos(request):
    #Busco todos los casos en principio
    casos = caso.objects.all()
    context = {'casos':casos}
    return render(request,'casos.html',context)
