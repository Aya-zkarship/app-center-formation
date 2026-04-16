from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom


class Formation(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField(default="Pas de description")
    niveau = models.CharField(max_length=50)
    duree = models.CharField(max_length=20)
    certification = models.CharField(max_length=100, default="Certifié")
    
    def __str__(self):
        return self.nom