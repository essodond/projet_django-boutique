# Configuration des routes URL pour l'application produits
from django.urls import path
from . import views

# Définition du nom de l'application pour les URL namespaces
app_name = 'produits'

# URLs de l'application produits
urlpatterns = [
    # Page d'accueil listant tous les produits
    path('', views.liste_produits, name='liste_produits'),                                    # Liste tous les produits

    # Affichage des détails d'un produit spécifique
    path('<int:produit_id>/', views.detail_produit, name='detail_produit'),                  # Détails d'un produit

    # Formulaire d'ajout d'un nouveau produit
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),                         # Ajouter un produit

    # Formulaire d'ajout d'une nouvelle catégorie
    path('ajouter_categorie/', views.ajouter_categorie, name='ajouter_categorie'),           # Ajouter une catégorie

    # Formulaire de modification d'un produit existant
    path('<int:produit_id>/modifier/', views.modifier_produit, name='modifier_produit'),      # Modifier un produit

    # Suppression d'un produit
    path('<int:produit_id>/supprimer/', views.supprimer_produit, name='supprimer_produit'),  # Supprimer un produit
    
    # Page des statistiques des produits
    path('statistiques/', views.statistiques_produits, name='statistiques_produits'),         # Statistiques des produits
]