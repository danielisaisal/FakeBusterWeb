from django.shortcuts import render
from django.http import HttpResponse
from . import principal

# Create your views here.
def mostrar_valor(request):
    if request.method == 'POST':
        autor = request.POST.get('autor')
        titulo = request.POST.get('titulo')
        fecha = request.POST.get('fecha')
        informacionAutor = principal.buscarInformacionDelAutor(autor)
        informacionTitulo = principal.buscarInformacionDelTitulo(titulo)
        informacionFecha = principal.informacionDeLaFecha(fecha,titulo)
        return render(request, 'index.html', {'valorAutor':informacionAutor, 'valorTitulo':informacionTitulo, 'valorFecha':informacionFecha})
    return render(request, 'index.html')
