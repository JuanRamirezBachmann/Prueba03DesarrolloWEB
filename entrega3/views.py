from django.shortcuts import render 
def index(request):
    return render(request, "index.html")
def servicios(request):
    return render(request, "Servicios.html")
def contacto(request):
    return render(request, "Contacto.html")
def galeriapacientes(request):
    return render(request, "galeriapacientes.html")
def medicosvet(request):
    return render(request, "MedicosVet.html")
def sobrenosotros(request):
    return render(request, "Sobrenosotros.html")