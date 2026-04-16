from django.db import models
import uuid

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    date_inscription = models.DateField(auto_now_add=True)
    code_acces = models.CharField(max_length=10, unique=True, default=uuid.uuid4)

    def __str__(self):
        return self.nom
