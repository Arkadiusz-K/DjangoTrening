from django.db import models

# Create your models here.

class Produkt(models.Model):
	nazwa = models.TextField(max_length=120)
	opis = models.TextField(blank=True)
	cena = models.TextField()
	podsumowanie=models.TextField(default="Django jest super")
	przecena = models.BooleanField()