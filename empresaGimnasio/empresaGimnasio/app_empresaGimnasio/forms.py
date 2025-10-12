from django import forms
from .models import Cliente , Servicio

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'


class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields='__all__'