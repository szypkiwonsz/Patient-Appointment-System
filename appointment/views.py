from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import DateForm
from .forms import AppointmentForm
from .models import Post

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
            date_selected = form.cleaned_data.get('date')
            name = form.cleaned_data.get('name')
            email_selected = form.cleaned_data.get('email')

            if date_selected.hour == 0:
                messages.warning(request, f'Proszę wybrać poprawną godzinę.')
                return redirect('appointment-wizyty')

            # Checks if first name is typed correctly without any numbers etc.
            elif name.isalpha() is not True:
                messages.warning(request, f'Niepoprawne imię.')
                return redirect('appointment-wizyty')

            else:
                date = Post.objects.raw('select * FROM appointment_post')
                for i in date:
                    if date_selected == i.date:
                        messages.warning(request, f'Wybrana data jest już zajęta.')
                        return redirect('appointment-wizyty')
                email = Post.objects.raw('select * FROM appointment_post')
                for i in email:
                    if email_selected == i.email:
                        messages.warning(request, f'Wybrany email jest już umówiony na wizytę.')
                        return redirect('appointment-wizyty')
                form.save()
                messages.success(request, f'Poprawnie umówiłeś wizytę.')
                return redirect('appointment-wizyty')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/wizyty.html', {'form': form})
