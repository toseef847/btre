from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requeset):
    # return HttpResponse('<h1>Hello World!</h1>')
    return render(requeset, 'pages/index.html')

def about(requeset):
    # return HttpResponse("You're at the pages")
    return render(requeset, 'pages/about.html')