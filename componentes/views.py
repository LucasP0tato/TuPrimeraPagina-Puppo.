from django.shortcuts import render, redirect
from .forms import ProcesadorForm, PlacaVideoForm, MotherboardForm, BusquedaProcesadorForm
from .models import Procesador

def home(request):
    return render(request, 'componentes/home.html')

def agregar_procesador(request):
    if request.method == 'POST':
        form = ProcesadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProcesadorForm()
    return render(request, 'componentes/formulario.html', {'form': form, 'titulo': 'Agregar Procesador'})

def buscar_procesador(request):
    resultados = []
    if request.method == 'GET':
        form = BusquedaProcesadorForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            if nombre:
                resultados = Procesador.objects.filter(nombre__icontains=nombre)
    else:
        form = BusquedaProcesadorForm()
    return render(request, 'componentes/buscar.html', {'form': form, 'resultados': resultados})