from django.db import models

class Devis(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    entreprise = models.CharField(max_length=100)
    domaine = models.CharField(max_length=100)
    intitule = models.CharField(max_length=100)
    participants = models.IntegerField()
    ville = models.CharField(max_length=100)
    details = models.TextField()

class Formation(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    niveau = models.CharField(max_length=50)
    duree = models.CharField(max_length=20)
    certification = models.CharField(max_length=100,default="Certifié")

    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    

    formations = models.ManyToManyField(Formation, blank=True)

    progression = models.IntegerField(default=0)

    certificat = models.FileField(upload_to='certificats/', blank=True, null=True)


    def __str__(self):
        return self.nom       
    

  


class Module(models.Model):
    TYPE_CHOICES = [
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('quiz', 'Quiz'),
    ]

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name='modules')
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to='modules/', blank=True, null=True)
    lien_video = models.URLField(blank=True, null=True)
    ordre = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.formation.titre} - {self.titre}"   