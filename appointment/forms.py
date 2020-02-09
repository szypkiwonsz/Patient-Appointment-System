from django import forms

from .models import Post


class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(label='Podaj datę wizyty:', input_formats=['%d.%m.%Y %H:%M'])

    class Meta:
        model = Post
        fields = ['date', 'name', 'email']