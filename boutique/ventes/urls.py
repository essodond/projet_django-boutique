# Configuration des routes locales pour ventes
from django.urls import path
from . import views

app_name = 'ventes'

urlpatterns = [
    path('', views.liste_ventes, name='liste_ventes'),
    path('<int:vente_id>/', views.detail_vente, name='detail_vente'),
    path('ajouter/', views.ajouter_vente, name='ajouter_vente'),
    path('<int:vente_id>/supprimer/', views.supprimer_vente, name='supprimer_vente'),
]
