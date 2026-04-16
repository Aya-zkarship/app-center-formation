from django.shortcuts import render
from .models import Formation

def index(request):
    formations = Formation.objects.all()
    print("FORMATIONS COUNT =", formations.count())   # debug مؤقت
    return render(request, 'index.html', {'formations': formations})

