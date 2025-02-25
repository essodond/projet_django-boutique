# Configuration des routes URL pour l'application ventes
from django.urls import path
from . import views

# Définition du nom de l'application pour les URL namespaces
app_name = 'ventes'

# URLs de l'application ventes
urlpatterns = [
    # Page d'accueil listant toutes les ventes
    path('', views.liste_ventes, name='liste_ventes'),                        # Liste toutes les ventes
    
    # Affichage des détails d'une vente spécifique
    path('<int:vente_id>/', views.detail_vente, name='detail_vente'),        # Détails d'une vente
    
    # Formulaire d'ajout d'une nouvelle vente
    path('ajouter/', views.ajouter_vente, name='ajouter_vente'),            # Ajouter une vente
    
    # Suppression d'une vente existante
    path('<int:vente_id>/supprimer/', views.supprimer_vente, name='supprimer_vente'),  # Supprimer une vente
]
