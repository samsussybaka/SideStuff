from django import forms
from core.models import Email

# Create your models here.
class EmailForm(forms.Form):
    Subject = forms.CharField(max_length=100)
    body = forms.CharField(max_length=1000)
    receiver = forms.CharField(max_length=100)
    sender = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    class Meta:
        model = Email
        fields = ['Subject', 'body','receiver', 'sender', 'password']