from django.db import models

# Create your models here.


class form(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    adderess = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class serviceform(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    services = models.CharField(max_length=50)
    adderess = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class need(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    adderess = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Donate(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    adderess = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.name
