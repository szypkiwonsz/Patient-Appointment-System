from django import forms

from .models import Post


class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(label='Provide date of visit:', input_formats=['%d.%m.%Y %H:%M'])

    class Meta:
        model = Post
        fields = ['date', 'name', 'email']


class AppointmentCancel(forms.Form):
    email = forms.EmailField(label='Enter the email address provided when registering the visit:')


class AppointmentCancelConfirm(forms.Form):
    key = forms.CharField(label='Enter the code sent to the email address provided to confirm your cancellation:')
