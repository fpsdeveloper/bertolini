from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from models import caso
from forms import casoForm

def index(request):
    return render(request,'indice.html')

#Listado Original de Casos
def casos(request):
    #Busco todos los casos en principio
    casos = caso.objects.all()
    context = {'casos':casos}
    return render(request,'casos.html',context)

#Formulario Caso
def casoFormulario(request):
    
    if request.method == 'POST':
        formulario = casoForm(request.POST)
        if formulario.is_valid():
            #hago algo con los datos
            datos = formulario.cleaned_data
            
            c = caso()
            c.numero = datos['numero']
            c.descripcion = datos['descripcion']
            c.expediente = datos['expediente']
            c.f = datos['f']
            c.jd = datos['jd']
            c.tribunal = datos['tribunal']
            c.save()

            return HttpResponseRedirect("/artcontrol/casos")
    elif request.method == 'GET':
        #obtengo el numero de caso seleccionado del listado
        numeroSeleccion = request.GET.get('numero','')
        #busco el caso en la capa de persistencia
        _caso = caso.objects.get(numero=numeroSeleccion)
        #inicializo el form con datos (bounded) 
        datos = {'numero':_caso.numero,
                'descripcion':_caso.descripcion,
                'expediente':_caso.expediente,
                'f':_caso.f,
                'JD':_caso.jd}

        formulario = casoForm(datos)

    return render(request, 'caso.html', {'formulario': formulario})
