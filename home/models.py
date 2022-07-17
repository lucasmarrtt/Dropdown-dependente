from django.db import models

# Create your models here.

class Estados(models.Model):
	nome = models.CharField(max_length=255)

	def __str__(self):
		return self.nome

class Cidades(models.Model):
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE)	
    nome = models.CharField(max_length=255)

    def __str__(self):
    	return self.nome


class Bairros(models.Model):
	cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
	nome = models.CharField(max_length=255)	

	def __str__(self):
		return f'{self.nome}, {self.cidade}'

