from django.shortcuts import render, redirect
from .models import Devis, Formation, Client, Inscription  # Regroupement des imports
from django.contrib import messages  # Import en haut du fichier

def index(request):
    formations = Formation.objects.all()
    print("FORMATIONS =", formations)
    print("COUNT =", formations.count())
    return render(request, 'index.html', {'formations': formations})

def devis(request):
    if request.method == "POST":
        # Validation des champs obligatoires
        if request.POST.get('nom') and request.POST.get('email'):  # Validation simplifiée
            Devis.objects.create(
                nom=request.POST.get('nom'),
                email=request.POST.get('email'),
                telephone=request.POST.get('telephone'),
                entreprise=request.POST.get('entreprise'),
                domaine=request.POST.get('domaine'),
                intitule=request.POST.get('intitule'),
                participants=request.POST.get('participants'),
                ville=request.POST.get('ville'),
                details=request.POST.get('details'),
            )
            messages.success(request, "Votre devis a été envoyé avec succès!")
            return redirect('devis')
        else:
            messages.error(request, "Veuillez remplir tous les champs obligatoires (nom et email).")
    
    return render(request, 'devis.html')

def client_login(request):
    error = None

    if request.method == "POST":
        code = request.POST.get("access_code")

        try:
            client = Client.objects.get(code_acces=code)
            request.session['client_id'] = client.id
            return redirect('client_dashboard')
        except Client.DoesNotExist:
            error = "Code invalide ❌"

    return render(request, "client_login.html", {"error": error})



def client_dashboard(request):
    client_id = request.session.get('client_id')

    if not client_id:
        return redirect('client_login')

    try:
        client = Client.objects.get(id=client_id)

        
        inscriptions = Inscription.objects.filter(client=client)

        return render(request, 'client.html', {
            'client': client,
            'inscriptions': inscriptions,
        })

    except Client.DoesNotExist:
        del request.session['client_id']
        return redirect('client_login')
    

def update_progress(request, inscription_id):
    ins = Inscription.objects.get(id=inscription_id)
    ins.progress += 20

    if ins.progress >= 100:
        ins.progress = 100
        ins.termine = True

    ins.save()
    return redirect('client_dashboard')   


def logout_view(request):
    request.session.flush()
    return redirect('client_login')











