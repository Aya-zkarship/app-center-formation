from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def devis_view(request):
    return render(request, 'devis.html')

def client_login(request):
    return render(request, 'login_client.html')

def client_dashboard(request):
    return render(request, 'client.html')

def admin_page(request):
    return render(request, 'admin.html')