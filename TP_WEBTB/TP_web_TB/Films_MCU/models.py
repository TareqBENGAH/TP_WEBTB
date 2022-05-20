from django.db import models
import django.utils.timezone
# Create your models here.
class Superhero(models.Model):
    nom = models.CharField(max_length=100,blank=False)
    date = models.DateField(blank=False, default=django.utils.timezone.now())
    createur = models.CharField(max_length=100,blank=False)
    acteurs = models.TextField(blank=False)
    super_pouvoir = models.TextField(blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return f"{self.nom}"

    def dico(self):
        return{"nom": self.nom, "date": self.date , "createur" : self.createur , "acteurs" : self.acteurs, "super_pouvoir" : self.super_pouvoir, "description" : self.description}

class Films(models.Model):
    nom_film = models.CharField(max_length=100,blank=False)
    superhero = models.ForeignKey(Superhero, on_delete=models.CASCADE, null="true")
    producteur = models.CharField(max_length=100)
    date = models.DateField(blank=False, default=django.utils.timezone.now())
    resume = models.TextField(blank=False)

    def __str__(self):
        return f"{self.nom_film}"

    def dico(self):
        return{"nom_film": self.nom_film, "superhero" : self.superhero, "producteur": self.producteur, "date": self.date, "resume": self.resume}