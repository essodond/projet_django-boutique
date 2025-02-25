from django import forms
from .models import Vente
from produits.models import Produit

class VenteForm(forms.ModelForm):
    """
    Formulaire pour la création et la modification des ventes.
    """
    produit_nom = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Nom du produit',
            'style': 'border-radius: 10px; padding: 10px;'
        })
    )
    
    quantite = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': 'Quantité',
            'min': '1',
            'style': 'border-radius: 10px; padding: 10px;'
        })
    )
    
    total = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-3',
            'placeholder': '0.00',
            'readonly': 'readonly',
            'style': 'border-radius: 10px; padding: 10px; background-color: #f8f9fa;'
        })
    )

    class Meta:
        model = Vente
        fields = ['produit_nom', 'quantite', 'total']
        labels = {
            'produit_nom': 'Nom du produit',
            'quantite': 'Quantité',
            'total': 'Total (FCFA)'
        }
        help_texts = {
            'produit_nom': 'Entrez le nom du produit',
            'quantite': 'Entrez la quantité à vendre',
            'total': 'Montant total de la vente'
        }

    def clean_quantite(self):
        quantite = self.cleaned_data.get('quantite')
        if quantite and quantite < 1:
            raise forms.ValidationError("La quantité doit être supérieure à 0")
        return quantite

    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total and total < 0:
            raise forms.ValidationError("Le total ne peut pas être négatif")
        return total