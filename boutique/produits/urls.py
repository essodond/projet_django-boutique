# Configuration des routes locales pour produits
from django.urls import path
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('ajouter_categorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('<int:produit_id>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('<int:produit_id>/supprimer/', views.supprimer_produit, name='supprimer_produit'),
    path('statistiques/', views.statistiques_produits, name='statistiques_produits'),

]