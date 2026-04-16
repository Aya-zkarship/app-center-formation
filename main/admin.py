from django.contrib import admin
from .models import Categorie, Formateur, Formation, Client, Paiement, Devis, Progression

admin.site.register(Categorie)
admin.site.register(Formateur)
admin.site.register(Formation)
admin.site.register(Client)
admin.site.register(Paiement)
admin.site.register(Devis)
admin.site.register(Progression)