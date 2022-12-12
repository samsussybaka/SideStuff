from django.db import models


class Email(models.Model):
    Subject = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    receiver = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    password = models.CharField(max_length=100)