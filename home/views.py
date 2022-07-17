from django.shortcuts import render
from . models import Cidades

from . forms import EstadosForm

# Create your views here.

def index(request):

	form = EstadosForm

	context = {
	    'form': form
	}
	return render(request, 'index.html', context)


def cities_choices_ajax(request):
	uf = request.GET.get('uf')

	cidades = Cidades.objects.filter(uf=uf)

	context = {'cidades': cidades}

	return render(request, 'cities_choices_ajax.html', context )
