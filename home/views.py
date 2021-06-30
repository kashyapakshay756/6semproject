from django.shortcuts import render, HttpResponse
from home.models import form
from .models import form
from home.models import serviceform
from home.models import Donate
from django.shortcuts import redirect

from home.models import need
from django.http import HttpResponse
from hello import settings
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):

   # if request.user.is_anonymous:
    #    return redirect("/loginuser")
    return render(request, 'index.html', )
    # return HttpResponse("this is homepage")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is aboutpage")


def Dashbord(request):
    return render(request, 'Dashbord.html')


def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is servicespage")


# def loginuser(request):
 #   if request.method == "POST":
  #
  #     print(username, password)
   #     user = authenticate(username='username', password='password')
    #    print(username, password)
    #      login(request, user)
    #      print(username, password)
    #     return redirect(request, '')
    # else:
    #   return render(request, 'login.html')

  #  return render(request, 'login.html')


def Donate(request):
  #  if request.method == "POST":
   #    email = request.POST.get('email')
    #    ser = request.POST.get('ser')
    #   adderess = request.POST.get('adderess')
    #  message = request.POST.get('message')
    # Donate = Donate(name=name, ser=ser, email=email,
    #                adderess=adderess, message=message)
    # Donate.save()

    return render(request, 'Donate.html')


def dsneed(request):
    return render(request, 'dsneed.html')


def dsdonate(request):
    return render(request, 'dsdonate.html')


def regestation(request):
    return render(request, 'regestation.html')


def dswork(request):
    return render(request, 'dswork.html')


def dsmedical(request):
    return render(request, 'dsmedical.html')


def dsdelivery(request):
    return render(request, 'dsdelivery.html')


def dsplumber(request):
    return render(request, 'dsplumber.html')


def home(request):
    return render(request, 'home.html')


def work(request):
    return render(request, 'work.html')


def emergency(request):
    return render(request, 'emergency.html')


def needhome(request):
    return render(request, 'needhome.html')


def gallery(request):
    return render(request, 'gallery.html')


def workwithus(request):
    return render(request, 'workwithus.html')


def dsblog(request):
    return render(request, 'dsblog.html')


def show(request):
    context = {}

    context['dataset'] = form.objects.all()

    return render(request, 'show.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        adderess = request.POST.get('adderess')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        contact = form(name=name, email=email, adderess=adderess,
                       mobile=mobile, password=password)
        contact.save()

    return render(request, 'contact.html')


def serviseform(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        services = request.POST.get('services')
        adderess = request.POST.get('adderess')
        message = request.POST.get('message')
        serviseform = serviceform(
            name=name, email=email, services=services, adderess=adderess, message=message)
        serviseform.save()

    return render(request, 'serviseform.html')


# return HttpResponse("this is contact page")


def need(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        servicess = request.POST.get('servicess')
        adderess = request.POST.get('adderess')
        message = request.POST.get('message')
        need = need(name=name, email=email, servicess=service,
                    adderess=adderess, message=message)
        need.save()

    return render(request, 'need.html')


def mail(request):
    subject = "Greetings"
    msg = "thanks for taking service from the NEED FOR HELP we are here to help you your services is approvied for the company over team will contact u as soon as posible "
    to = "irfan.sssit@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if(res == 1):
        msg = "service has been aprovied by the company <button>back to home page</button>"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)
