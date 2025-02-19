from django import forms
from .models import Produit
from .models import Categorie

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nom de la catégorie'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description de la catégorie'}),
        }

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'stock', 'categorie']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'group'})


