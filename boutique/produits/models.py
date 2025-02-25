from django.db import models

# Modèles pour l'application produits

class Categorie(models.Model):
    """
    Modèle représentant une catégorie de produits.

    """
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nom

class Produit(models.Model):
    """
    Modèle représentant un produit dans la boutique.
    
    """
    nom = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produits')
    
    def __str__(self):
        return self.nom