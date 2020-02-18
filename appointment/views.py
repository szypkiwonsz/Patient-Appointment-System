from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm, AppointmentCancel, AppointmentCancelConfirm
from .models import Post
from .methods import DateTime
from django.core.mail import EmailMessage


# Create your views here.
def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')

            if date.hour == 0:
                messages.warning(request, f'Please select the correct time.')
                return redirect('appointment-make_appointment')

            # Checks if first name is typed correctly without any numbers etc.
            elif name.isalpha() is not True:
                messages.warning(request, f'Incorrect name.')
                return redirect('appointment-make_appointment')

            else:
                data = Post.objects.raw('select * FROM appointment_post')
                for i in data:
                    if date == i.date:
                        messages.warning(request, f'Selected date is already taken.')
                        return redirect('appointment-make_appointment')
                for i in data:
                    if email == i.email:
                        messages.warning(request, f'Selected email is already scheduled for the visit.')
                        return redirect('appointment-make_appointment')
                form.save()
                subject = 'Appointment - {}'.format(email)
                message = "{} was appointed for {}:{} on day {}.{}.{}. " \
                          "Confirm the visit by replying to the patient's email: {}".format(name,
                                                                                            DateTime.add_zero(
                                                                                                date.hour),
                                                                                            DateTime.add_zero(
                                                                                                date.minute),
                                                                                            DateTime.add_zero(date.day),
                                                                                            DateTime.add_zero(
                                                                                                date.month),
                                                                                            DateTime.add_zero(
                                                                                                date.year),
                                                                                            email)
                email = EmailMessage(subject, message, to=['ADMIN EMAIL ADRESS'])
                email.send()
                subject = 'Your appointment on fizjo-med has been correctly arranged'
                message = 'You have been correctly arranged to visit for {}:{} on day {}.{}.{}. ' \
                          'If you want to cancel your visit, use the form on our website.'.format(
                            DateTime.add_zero(date.hour),
                            DateTime.add_zero(date.minute),
                            DateTime.add_zero(date.day),
                            DateTime.add_zero(date.month),
                            DateTime.add_zero(date.year))
                email = EmailMessage(subject, message, to=[email])
                email.send()
                messages.success(request, f'You have made an appointment correctly.')
                return redirect('appointment-make_appointment')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/make_appointment.html', {'form': form})


def cancel_appointment(request):
    key = None
    if request.method == 'POST':
        form = AppointmentCancel(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            data = Post.objects.raw('select * FROM appointment_post')
            for i in data:
                if email == i.email:
                    key = i.key
            if key is None:
                messages.warning(request, f'There is no email address provided in the database.')
                return redirect('appointment-cancel_appointment')

            subject = "Your code to cancel your visit"

            email = EmailMessage(subject, key, to=[email])
            email.send()
            return redirect('appointment-confirm_cancel_appointment')
    else:
        form = AppointmentCancel()
    return render(request, 'appointment/cancel_appointment.html', {'form': form})


def confirm_cancel_appointment(request):
    if request.method == 'POST':
        form = AppointmentCancelConfirm(request.POST)
        if form.is_valid():
            key = form.cleaned_data.get('key')
            data = Post.objects.raw('select * FROM appointment_post')
            for i in data:
                if key == i.key:
                    Post.objects.filter(key=key).delete()
                    messages.success(request, f'You have successfully canceled your visit.')
                    return redirect('appointment-make_appointment')
            messages.warning(request, f'Incorrect key.')
            return redirect('appointment-cancel_appointment')
    else:
        form = AppointmentCancelConfirm()
    return render(request, 'appointment/confirm_cancel_appointment.html', {'form': form})
