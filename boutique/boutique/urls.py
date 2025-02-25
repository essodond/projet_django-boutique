"""
Configuration des URLs principales du projet boutique.

Ce fichier définit les routes URL principales de l'application, incluant :
- Les URLs de l'application produits
- Les URLs de l'application ventes
- Les URLs de l'interface d'administration Django
"""

from django.contrib import admin
from django.urls import path, include

# Configuration des patterns d'URL principaux
urlpatterns = [
    # Interface d'administration Django
    path('admin/', admin.site.urls),
    
    # URLs de l'application produits (gestion des produits et catégories)
    path('produits/', include('produits.urls', namespace='produits')),
    
    # URLs de l'application ventes (gestion des ventes et transactions)
    path('ventes/', include('ventes.urls', namespace='ventes')),
]
