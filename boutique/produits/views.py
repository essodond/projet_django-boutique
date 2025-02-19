from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produit, Categorie
from .forms import ProduitForm
from django.db.models import Sum, Avg, Count

# filepath: /c:/Users/DELL/Desktop/COURS/projet djamgo/boutique/produits/views.py
from django.shortcuts import render, redirect
from .forms import CategorieForm

def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits:liste_produits')
    else:
        form = CategorieForm()
    return render(request, 'produits/ajouter_categorie.html', {'form': form})

# Create your views here.
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits/liste_produits.html', {'produits': produits})

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'produits/detail_produit.html', {'produit': produit})

def ajouter_produit(request):
    if request.method == "POST":
        nom = request.POST['nom']
        description = request.POST['description']
        prix = request.POST['prix']
        stock = request.POST['stock']
        categorie_id = request.POST['categorie']
        categorie = get_object_or_404(Categorie, id=categorie_id)
        Produit.objects.create(nom=nom, description=description, prix=prix, stock=stock, categorie=categorie)
        return HttpResponseRedirect(reverse('liste_produits'))
    categories = Categorie.objects.all()
    return render(request, 'produits/ajouter_produit.html', {'categories': categories})




def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    produit.delete()
    return HttpResponseRedirect(reverse('liste_produits'))

def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    if request.method == "POST":
        produit.nom = request.POST['nom']
        produit.description = request.POST['description']
        produit.prix = request.POST['prix']
        produit.stock = request.POST['stock']
        produit.categorie = get_object_or_404(Categorie, id=request.POST['categorie'])
        produit.save()
        return HttpResponseRedirect(reverse('liste_produits'))
    categories = Categorie.objects.all()
    return render(request, 'produits/modifier_produit.html', {'produit': produit, 'categories': categories})

def ajouter_produit(request):
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits:liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/ajouter_produit.html', {'form': form})

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

    
## views pour categorie

# filepath: /c:/Users/DELL/Desktop/COURS/projet djamgo/boutique/produits/views.py


def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produits:liste_produits')
    else:
        form = CategorieForm()
    return render(request, 'produits/ajouter_categorie.html', {'form': form})




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