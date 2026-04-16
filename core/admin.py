from django.contrib import admin
from .models import Formation, Devis, Client,Module


admin.site.register(Formation)
admin.site.register(Module)
admin.site.register(Devis)
admin.site.register(Client)