from django.shortcuts import render


# Create your views here.
def index(response):
    return render(response, 'appointment/index.html')


def uslugi(response):
    return render(response, 'appointment/uslugi.html')


def cennik(response):
    return render(response, 'appointment/cennik.html')


def o_mnie(response):
    return render(response, 'appointment/o_mnie.html')
