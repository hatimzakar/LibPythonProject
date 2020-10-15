from django.shortcuts import render, redirect
from .form import ProduitForm,FactureForm
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from .models import Produit, Facture


# Create your views here.

@login_required(login_url='/register/login/')
def AjouterProduit(request):

        form = ProduitForm()
        if request.method == 'POST':
            form = ProduitForm(request.POST)
            print(form)
            if form.is_valid():
                print("formvalid ;;")

                form.save()
                return redirect('/library/AfficherProduit')


            else:
                print("form  not valdi")

        context = {'ProduitForm': ProduitForm}
        return render(request, 'produit.html', context)



@login_required(login_url='/register/login/')
def Update(request,pk):
    produit= Produit.objects.get(id=pk)
    print("NIV 1")
    if request.method=='POST':
        print("niv 2")
        form=ProduitForm(request.POST,instance=produit)
        print(form)
        if form.is_valid():
            print(form)
            print("niv3")
            form.save()
            return redirect('/library/AfficherProduit')
    print("niv 0")
    return render(request,'index.html')


@login_required(login_url='/register/login/')
def ModifierProduit(request,pk):


    produit = Produit.objects.get(id=pk)
    return render(request, 'ModifierProduit.html', {'produit':produit})



@login_required(login_url='/register/login/')
def AfficherProduit(request):

    objects = Produit.objects.all().order_by('designation');
    context = {'produits': objects}

    return render(request, 'tables.html', context)

@login_required(login_url='/register/login/')
def Delete(request,pk):

    produit=Produit.objects.get(id=pk)
    produit.delete()
    return redirect('/library/AfficherProduit')
@login_required(login_url='/register/login/')
def AjouterFacture(request):




    form = FactureForm()
    if request.method == 'POST':
        form = FactureForm(request.POST)
        print(form)
        if form.is_valid():
            print("formvalid ;;")

            form.save()
            return redirect('/library/AfficherFacture')


        else:
            print("form  not valdi")


    return render(request, 'facture.html')
@login_required(login_url='/register/login/')
def AfficherFacture(request):
    factures = Facture.objects.all()
    context = {'factures': factures}

    return render(request, 'TableFacture.html', context)
@login_required(login_url='/register/login/')
def editFacture(request,pk):
    facture = Facture.objects.get(id=pk)
    return render(request, 'ModifierFacture.html', {'facture': facture})

@login_required(login_url='/register/login/')
def UpdateFacture(request,pk):
    facture = Facture.objects.get(id=pk)
    print("NIV 1")
    if request.method == 'POST':
        print("niv 2")
        form = FactureForm(request.POST, instance=facture)
        print(form)
        if form.is_valid():
            print(form)
            print("niv3")
            form.save()
            return redirect('/library/AfficherFacture')
    print("niv 0")
    return render(request, 'index.html')

@login_required(login_url='/register/login/')
def DeleteFac(request,pk):
    facture=Facture.objects.get(id=pk)
    facture.delete()
    return redirect('/library/AfficherProduit')

def Facture2(request):

    return render(request,"Facture2.html")


