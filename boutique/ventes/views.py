from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Vente
from .forms import VenteForm
from django.shortcuts import redirect
from django.db.models import Sum, Avg

# Create your views here.
# Définition des vues pour l'application ventes

# Liste toutes les ventes
def liste_ventes(request):
    ventes = Vente.objects.all()
    context = {
        'ventes': ventes,
        'total_ventes': ventes.aggregate(Sum('total'))['total__sum'] or 0,
        'moyenne_vente': ventes.aggregate(Avg('total'))['total__avg'] or 0
    }
    return render(request, 'ventes/liste_ventes.html', context)



# Affiche les détails d'une vente
def detail_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    return render(request, 'ventes/detail_vente.html', {'vente': vente})



# Ajoute une nouvelle vente
def ajouter_vente(request):
    if request.method == "POST":
        form = VenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventes:liste_ventes')
    else:
        form = VenteForm()
    return render(request, 'ventes/ajouter_vente.html', {'form': form})



# Supprime une vente
def supprimer_vente(request, vente_id):
    vente = get_object_or_404(Vente, id=vente_id)
    vente.delete()
    return HttpResponseRedirect(reverse('ventes:liste_ventes'))