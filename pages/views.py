from django.shortcuts import render
# from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(requeset):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }
    # return HttpResponse('<h1>Hello World!</h1>')
    return render(requeset, 'pages/index.html', context)

def about(requeset):
    # All realtors
    all_realtors = Realtor.objects.order_by('hire_date')

    # Realtor(s) of the month
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    # The context object
    context = {
        'realtors': all_realtors,
        'mvp_realtor': mvp_realtors,
    }
    # return HttpResponse("You're at the pages")
    return render(requeset, 'pages/about.html', context)