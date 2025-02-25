from django.db import models
from produits.models import Produit 

# Modèle pour gérer les ventes
class Vente(models.Model):
    """
    Modèle représentant une vente.
    
    """
    date = models.DateTimeField(auto_now_add=True)
    produit_nom = models.CharField(max_length=100, default='Default Product Name')
    quantite = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Vente du {self.date.strftime('%d-%m-%Y %H:%M')} - {self.produit.nom}"

# Modèle pour gérer les lignes de vente (détails d'une vente)
class LigneVente(models.Model):
    """
    Modèle représentant une ligne de vente.
    
    """
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name='lignes')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"