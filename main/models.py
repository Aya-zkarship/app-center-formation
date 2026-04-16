from django.db import models
import random
import string

# --------------------------
# Générateur code d'accès
# --------------------------
def generer_code_acces():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))


# --------------------------
# Catégorie
# --------------------------
class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


# --------------------------
# Formateur
# --------------------------
class Formateur(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.nom


# --------------------------
# Formation
# --------------------------
class Formation(models.Model):
    image = models.ImageField(upload_to='formations/', blank=True, null=True)
    nom = models.CharField(max_length=150)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    formateur = models.ForeignKey(Formateur, on_delete=models.SET_NULL, null=True, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    duree = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


# --------------------------
# Client
# --------------------------
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    date_inscription = models.DateField()
    formations = models.ManyToManyField(Formation, blank=True)
    code_acces = models.CharField(max_length=20, unique=True, default=generer_code_acces)

    def __str__(self):
        return self.nom


# --------------------------
# Paiement
# --------------------------
class Paiement(models.Model):
    STATUT_CHOICES = [
        ('Payé', 'Payé'),
        ('En attente', 'En attente'),
        ('Échoué', 'Échoué'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.client.nom} - {self.formation.nom}"


# --------------------------
# Devis
# --------------------------
class Devis(models.Model):
    nom_complet = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    entreprise = models.CharField(max_length=150)
    domaine_formation = models.CharField(max_length=150)
    intitule_formation = models.CharField(max_length=150)
    nombre_participants = models.PositiveIntegerField()
    ville_formation = models.CharField(max_length=100)
    details_demande = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_complet


# --------------------------
# Progression
# --------------------------
class Progression(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    progression = models.PositiveIntegerField(default=0)
    certificat_disponible = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.nom} - {self.formation.nom} ({self.progression}%)"
