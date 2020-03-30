from django.shortcuts import render
from django.core.mail import send_mail

from mailgmail import forms
from mailsending.settings import EMAIL_HOST_USER


def subscribe(request):
    form = forms.DMail
    if request.method == 'POST':
        form = forms.DMail(request.POST)
        subject = 'Welcome to SMTP Mail'
        message = 'Hope you are enjoying your Django Mail Sending code'
        recipient = str(form['email'].value())

        send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)

        return render(request, 'index.html', {'recipient': recipient})
    return render(request, 'index.html', {'form': form})
