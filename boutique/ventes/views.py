from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Vente

# Create your views here.
# Définition des vues pour l'application ventes


# Définition des vues pour l'application ventes
def liste_ventes(request):
    ventes = Vente.objects.all()
    return render(request, 'ventes/liste_ventes.html', {'ventes': ventes})

def detail_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    return render(request, 'ventes/detail_vente.html', {'vente': vente})

def ajouter_vente(request):
    if request.method == "POST":
        total = request.POST['total']
        vente = Vente.objects.create(total=total)
        return HttpResponseRedirect(reverse('ventes:liste_ventes'))
    return render(request, 'ventes/ajouter_vente.html')

def supprimer_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    vente.delete()
    return HttpResponseRedirect(reverse('ventes:liste_ventes'))

