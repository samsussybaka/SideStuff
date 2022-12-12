from django.shortcuts import render
from .forms import EmailForm
import smtplib
import ssl
from email.message import EmailMessage
# Create your views here.

def homepage(request):
    if request.method == "POST":

        form = EmailForm(request.POST)

        email_sender = form.data['sender']
        email_password = form.data['password']
        email_receiver = form.data['receiver']
        subject = form.data['Subject']
        body = form.data['body']

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    return render(request, 'core/index.html')