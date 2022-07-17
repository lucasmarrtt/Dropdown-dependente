from django.forms import ModelForm, Form 
from . models import Estados, Cidades, Bairros
from django import forms

# Create the form class.

# Usamos isso caso queiramos exibir select de ForeignKey 
class EstadosForm(forms.Form):
	state = forms.ModelChoiceField(label='Estados', queryset=Estados.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    