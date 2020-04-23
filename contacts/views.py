from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
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

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id = listing_id, user_id = user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquery to this property.')
                return redirect('/listings/'+listing_id)

        contact = Contacts(listing = listing, listing_id = listing_id, name= name, email = email, phone = phone, message = message, user_id = user_id )

        contact.save()

        send_mail(
            'Property Listing Inquiry',
            'Hello Realtor! There is a new inquery for'+ listing + 'Visit Admin Panel for more info.',
            'toseefhasan@gmail.com',
            [realtor_email, 'qasim@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
        return redirect('/listings/'+listing_id)
