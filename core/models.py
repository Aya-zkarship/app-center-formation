from django.db import models
import random
import string

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
    formateur = models.CharField(max_length=100, default="Inconnu")
    def __str__(self):
        return self.nom


class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    
    code_acces = models.CharField(max_length=10, unique=True, blank=True)
    
    progression = models.IntegerField(default=0)

    certificat = models.FileField(upload_to='certificats/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code_acces:
            self.code_acces = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        super().save(*args, **kwargs)
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
    type = models.CharField(
    max_length=20,
    choices=TYPE_CHOICES,
    default='video'
)
    fichier = models.FileField(upload_to='modules/', blank=True, null=True)
    lien_video = models.URLField(blank=True, null=True)
    ordre = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.formation.nom} - {self.titre}"
    
class Inscription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    date_inscription = models.DateField(auto_now_add=True)
    
    progress = models.IntegerField(default=0)  # 0 -> 100
    termine = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.nom} - {self.formation.nom}"


class Certificat(models.Model):
    inscription = models.OneToOneField(Inscription, on_delete=models.CASCADE)
    date_obtention = models.DateField(auto_now_add=True)
    code_certificat = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.code_certificat
    
class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="quizzes")
    question = models.TextField()

    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)

    correct_answer = models.CharField(
        max_length=1,
        choices=[
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
        ]
    )

    def __str__(self):
        return self.question  

