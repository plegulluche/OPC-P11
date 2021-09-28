from django.shortcuts import render, redirect

from userauth.forms import Adduserform
from userauth.models import Users


def authpage(request):
    
    return render(request, 'authenticate.html')


def create_user(request):
    if request.method == "GET":
        form = Adduserform()
        return render(request, 'adduser.html', {'form': form})
    elif request.method == "POST":
        form = Adduserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authpage')
        else:
            return redirect('add_user')