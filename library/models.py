from django.db import models

# Create your models here.




class Produit(models.Model):


         numero=models.IntegerField(max_length=100)
         designation=models.CharField(max_length=100)
         prix=models.FloatField(default=0)
         quantite=models.IntegerField(default=0)


         class Meta:
             ordering = ('designation',)

class Facture(models.Model):
        numero=models.IntegerField(max_length=100)
        nom = models.CharField(max_length=100)
        prenom = models.CharField(max_length=100)
        numeroProduit=models.ForeignKey(Produit,on_delete=models.CASCADE)
        quantite=models.IntegerField(max_length=100)


