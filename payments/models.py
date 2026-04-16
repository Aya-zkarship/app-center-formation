from django.db import models
from accounts.models import Client
from formations.models import Formation

class Paiement(models.Model):
    STATUT_CHOICES = [
        ('paye', 'Payé'),
        ('en_attente', 'En attente'),
        ('echoue', 'Échoué'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    montant = models.FloatField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    date = models.DateField(auto_now_add=True)