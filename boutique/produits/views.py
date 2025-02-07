from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Produit, Categorie

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
