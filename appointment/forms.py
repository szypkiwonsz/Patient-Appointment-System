from django import forms

from .models import Post


class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(label='Podaj datę wizyty:', input_formats=['%d.%m.%Y %H:%M'])

    class Meta:
        model = Post
        fields = ['date', 'name', 'email']


class AppointmentCancel(forms.Form):
    email = forms.EmailField(label='Podaj adres email podany przy rejestracji wizyty:')


class AppointmentCancelConfirm(forms.Form):
    key = forms.CharField(label='Podaj kod wysłany na podany adres email, by potwierdzić odwołanie wizyty.')
