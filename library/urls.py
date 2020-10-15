from django.contrib import admin
from django.urls import path
from . import views



urlpatterns= [
        path('AjouterProduit/',views.AjouterProduit,name="AjouterProduit"),
        path('AfficherProduit/', views.AfficherProduit, name="AffiherProduit"),
        path('ModifierProduit/<str:pk>/', views.ModifierProduit, name="ModifierProduit"),
        path('Update/<str:pk>/', views.Update, name="Update"),
        path('Delete/<str:pk>/', views.Delete, name="Delete"),
        path('AjouterFacture/', views.AjouterFacture, name="AjouterFacture"),
        path('AfficherFacture/', views.AfficherFacture, name="AfficherFacture"),
        path('editFacture/<str:pk>/', views.editFacture, name="editFacture"),
        path('UpdateFacture/<str:pk>/', views.UpdateFacture, name="UpdateFacture"),
        path('DeleteFac/<str:pk>/', views.DeleteFac, name="DeleteFac"),
        path('Facture2/', views.Facture2, name="Facture2")




                    ]
