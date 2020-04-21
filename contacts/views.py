from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacts
# from django.http import request

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = request.POST['realtor_email']
        user_id = request.POST['user_id']
        print(user_id)

        contact = Contacts(listing = listing, listing_id = listing_id, name= name, email = email, phone = phone, message = message, user_id = user_id )

        contact.save()

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)