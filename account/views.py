from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.template.loader import render_to_string
from account.forms import  AccountAuthenticationForm
from uuid import uuid4
from account.models import Account
from purbeurre.manager import send_mail

def activate_message_view(request):
    return render(request, 'activate_email.html')

def active_succes_view(request):
    return render(request, 'active_success.html')

def activate_email_view(request,token):
    user = Account.objects.filter(token=token).first()
    if user:
        user.email_is_active = True
        user.save()
        return redirect('success')
    else:
        return redirect('login')


def registration_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name, email, password)
        rand_token = uuid4()
        
        new_user = Account()
        new_user.username = name
        new_user.email = email
        new_user.password = password
        new_user.token = rand_token
        new_user.save()
        new_user.set_password(password)
        new_user.save()
        
        subject = 'activez votre compte'
        content = render_to_string(
            "active.html",
            {
                "username": name,
                "link": f'http://127.0.0.1:8000/activate-email/{rand_token}'
                
            },
        )
        send_mail(email,subject,content)
        return redirect('activate_your_mail')
    return render(request,'register.html')
    
def logout_view(request):
    logout(request)
    return redirect('mainpage')


def login_view(request):
    
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Account.objects.filter(email=email, is_active=True).first()
        if user:
            utilisateur_auth = authenticate(email=user.email, password=password)
            if utilisateur_auth:
                if user.email_is_active:
                    login(request, utilisateur_auth)
                    return redirect('mainpage')
                else:
                    message = "merci d'activer votre compte"
            else:
                message = "vos identifiants ne sont pas corrects"
        else:
            message = "aucun utilisateur ne correspond a vos informations saisies"
    
    return render(request, 'login.html', {"message":message})      

def account_view(request):
    
    return render(request,'account_page.html', {})






