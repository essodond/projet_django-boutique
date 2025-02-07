# Configuration des routes locales pour produits
from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('<int:produit_id>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('<int:produit_id>/supprimer/', views.supprimer_produit, name='supprimer_produit'),
]