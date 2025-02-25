from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produit, Categorie
from .forms import ProduitForm, CategorieForm
from django.db.models import Sum, Avg, Count, F

# Affiche la liste de tous les produits
def liste_produits(request):
    produits = Produit.objects.all()
    # Calcul de la valeur totale du stock (prix * quantité pour chaque produit)
    valeur_stock = produits.aggregate(
        total=Sum(F('prix') * F('stock'))
    )['total'] or 0
    
    context = {
        'produits': produits,
        'valeur_stock': valeur_stock
    }
    return render(request, 'produits/liste_produits.html', context)


# Affiche les détails d'un produit
def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'produits/detail_produit.html', {'produit': produit})


# Ajoute un nouveau produit
def ajouter_produit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits:liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/ajouter_produit.html', {'form': form})


# Modifie un produit existant
def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == "POST":
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produits:liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produits/modifier_produit.html', {'form': form})


# Supprime un produit
def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produit.delete()
    return HttpResponseRedirect(reverse('liste_produits'))


# Ajoute une nouvelle catégorie
def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits:liste_produits')
    else:
        form = CategorieForm()
    return render(request, 'produits/ajouter_categorie.html', {'form': form})


# Affiche les statistiques des produits
def statistiques_produits(request):
    total_produits = Produit.objects.count()
    total_stock = Produit.objects.aggregate(Sum('stock'))['stock__sum']
    prix_moyen = Produit.objects.aggregate(Avg('prix'))['prix__avg']
    categorie_populaire = Produit.objects.values('categorie__nom').annotate(count=Count('id')).order_by('-count').first()

    context = {
        'total_produits': total_produits,
        'total_stock': total_stock,
        'prix_moyen': prix_moyen,
        'categorie_populaire': categorie_populaire['categorie__nom'] if categorie_populaire else None,
    }
    return render(request, 'produits/statistiques.html', context)