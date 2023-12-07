from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from django.http import HttpResponse
from .models import Contact


def index(request):
    mylist = ""
    for contact in Contact.objects.all().order_by("first_name", "last_name"):
        mylist += f"{contact.first_name} {contact.last_name}<br>"
    return HttpResponse(
        "<div style='text-align: center; padding: 20px; background-color: #f0f0f0; border-radius: 10px;'><h2>All Contacts:</h2>"
        + mylist
        + "</div>"
    )
