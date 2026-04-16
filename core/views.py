from django.shortcuts import render, redirect
from .models import Devis
from .models import Formation  # Add this missing import
from .models import Client

def index(request):
    formations = Formation.objects.all()
    print("FORMATIONS =", formations)
    print("COUNT =", formations.count())
    return render(request, 'index.html', {'formations': formations})

def devis(request):
    if request.method == "POST":
        # Add validation to prevent empty submissions
        if all(request.POST.get(field) for field in ['nom', 'email']):  # Basic validation
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
            # Add success message (optional)
            from django.contrib import messages
            messages.success(request, "Votre devis a été envoyé avec succès!")
            return redirect('devis')
        else:
            # Handle validation error
            from django.contrib import messages
            messages.error(request, "Veuillez remplir tous les champs obligatoires.")
    
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
        return redirect('client_dashboard')

    client = Client.objects.get(id=client_id)

    return render(request, 'client.html', {'client': client})


def client_dashboard(request):
    client_id = request.session.get('client_id')

    if not client_id:
        return redirect('client_dashboard')

    client = Client.objects.get(id=client_id)

    return render(request, 'client.html', {
        'client': client
    })

def client_dashboard(request):
    client_id = request.session.get('client_id')

    if not client_id:
        return redirect('client_login')

    client = Client.objects.get(id=client_id)

    modules = client.formation.modules.all().order_by('ordre')

    return render(request, 'client.html', {
        'client': client,
        'modules': modules
    })