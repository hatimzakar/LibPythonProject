from django.forms import ModelForm
from .models import Produit,Facture
from django import forms


class ProduitForm(ModelForm):
    class Meta:
        model=Produit
        fields='__all__'

class FactureForm(ModelForm):
    class Meta:
        model=Facture
        fields='__all__'




