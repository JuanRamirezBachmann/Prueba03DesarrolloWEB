from django.shortcuts import render 
def index(request):
    return render(request, "index.html")
def servicios(request):
    return render(request, "Servicios.html")
def contacto(request):
    return render(request, "Contacto.html")