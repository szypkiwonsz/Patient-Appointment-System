from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import DateForm
from .forms import AppointmentForm


# Create your views here.
def index(response):
    return render(response, 'appointment/index.html')


def uslugi(response):
    return render(response, 'appointment/uslugi.html')


def cennik(response):
    return render(response, 'appointment/cennik.html')


def o_mnie(response):
    return render(response, 'appointment/o_mnie.html')


def wizyty(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            if date.hour == 0:
                messages.warning(request, f'Nie można wybrać tej godziny!')
                return redirect('appointment-wizyty')
            else:
                form.save()
                messages.success(request, f'Poprawnie umówiłeś wizytę.')
                return redirect('appointment-index')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/wizyty.html', {'form': form})