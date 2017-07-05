from django import forms
from artcontrol.models import juzgado

class casoForm(forms.Form):
    numero = forms.IntegerField(label="Numero")
    descripcion = forms.CharField(label="Descripcion", max_length=200)
    expediente = forms.CharField(label="Expediente",max_length=100)
    f = forms.CharField(label="f",max_length=20)
    jd = forms.CharField(label="JD",max_length=200)
    tribunal = forms.ModelChoiceField(queryset = juzgado.objects.all())

