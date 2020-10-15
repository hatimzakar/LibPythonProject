from django.contrib import admin
from .models import Produit,Facture
# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Facture)