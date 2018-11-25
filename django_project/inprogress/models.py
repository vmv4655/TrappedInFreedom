from django.db import models

# Create your models here.

class WelcomeMessage(models.Model):
	"""
	Mensaje de bienvenida a la pagina
	"""
	message = models.CharField(max_length=200)

	def __str__(self):
		return self.message