from django.shortcuts import render


def mainpage(request):
    context = {}

    return render(request, "mainpage.html", context)


def legalpage(request):

    return render(request, "legals.html", {})


def handle_not_found(request, exception):
    return render(request, "not-found.html")
