from django import forms
from .models import Vente

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['produit_nom', 'quantite', 'total']