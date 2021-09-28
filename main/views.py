from django.shortcuts import render
from userauth.models import Users


def mainpage(request):
    users = Users.objects.all()
    return render(request, 'mainpage.html')
