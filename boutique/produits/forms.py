from django import forms
from .models import Produit
from .models import Categorie


"""
    Formulaire pour la création et la modification des catégories.
    
"""
class CategorieForm(forms.ModelForm):

    class Meta:
        model = Categorie
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de la catégorie'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description de la catégorie'
            }),
        }


"""
    Formulaire pour la création et la modification des produits.
    
"""
class ProduitForm(forms.ModelForm):
   
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'stock', 'categorie']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Nom du produit',
                'style': 'border-radius: 10px; padding: 10px;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Description détaillée du produit',
                'rows': 4,
                'style': 'border-radius: 10px; padding: 10px;'
            }),
            'prix': forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': '0.00',
                'min': '0',
                'step': '0.01',
                'style': 'border-radius: 10px; padding: 10px;'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Quantité en stock',
                'min': '0',
                'style': 'border-radius: 10px; padding: 10px;'
            }),
            'categorie': forms.Select(attrs={
                'class': 'form-select mb-3',
                'style': 'border-radius: 10px; padding: 10px;'
            })
        }
        labels = {
            'nom': 'Nom du produit',
            'description': 'Description',
            'prix': 'Prix (FCFA)',
            'stock': 'Stock disponible',
            'categorie': 'Catégorie'
        }

    def __init__(self, *args, **kwargs):
        """
        Initialise le formulaire en ajoutant la classe 'group' à tous les champs
        pour une mise en forme cohérente.
        """
        super().__init__(*args, **kwargs)
        # Ajout des classes Bootstrap et des styles pour les labels
        for field in self.fields.values():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' shadow-sm'
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select mb-3 shadow-sm'
            else:
                field.widget.attrs['class'] = 'form-control mb-3 shadow-sm'
            field.widget.attrs['style'] = 'border-radius: 10px; padding: 10px;'

    def clean_prix(self):
        prix = self.cleaned_data.get('prix')
        if prix and prix < 0:
            raise forms.ValidationError("Le prix ne peut pas être négatif")
        return prix

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock and stock < 0:
            raise forms.ValidationError("Le stock ne peut pas être négatif")
        return stock
