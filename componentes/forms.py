from django import forms
from .models import Procesador, PlacaVideo, Motherboard

class ProcesadorForm(forms.ModelForm):
    class Meta:
        model = Procesador
        fields = '__all__'

class PlacaVideoForm(forms.ModelForm):
    class Meta:
        model = PlacaVideo
        fields = '__all__'

class MotherboardForm(forms.ModelForm):
    class Meta:
        model = Motherboard
        fields = '__all__'

class BusquedaProcesadorForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, label='Buscar procesador por nombre')