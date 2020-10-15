from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
      username1 = request.POST['username']
      password2 = request.POST['password']

      user2 = auth.authenticate(username=username1, password=password2)
      if user2 is not None:
         auth.login(request, user2)
         print(user2)
         return redirect('/library/AfficherProduit')
      else:
           print(user2)
           messages.info(request,'Wrong Password')

           return redirect('/register/login')

    else:
      return render(request,'login_form.html')




def logout(request):

    auth.logout(request)
    return render(request,'index.html')








def register(request ):
      if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            print('User Taken')
        elif User.objects.filter(email=email).exists():
            print('Email Taken')
        else:
            user= User.objects.create_user(username=username,password=password,email=email)
            user.save()
            return redirect('/register/login')
      else:

       return render(request,'register.html')

