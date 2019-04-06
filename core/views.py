from django.shortcuts import render, HttpResponse


# Create your views here.

# Vista que retorna la plantilla Inicio
def home(request):
    return render(request, 'core/home.html')

# Vista que retorna la plantilla Acerca-de
def about(request):
    return render(request, 'core/about.html')

# Vista que retorna la plantilla Contacto
def contact(request):
    return render(request, 'core/contact.html')
