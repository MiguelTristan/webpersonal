from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    projects=Project.objects.all()
    # La variable 'projects' es una lista de objetos y se la pase como parametro a la pagina que esta en esta funcion
    return render(request, 'portfolio/portfolio.html', {'projects':projects})
