from django.shortcuts import render

# Create your views here.

def home(request):
    """Home page view"""
    context = {
        'title': 'Barbarossa Live - Home',
        'page_title': 'Welcome to Barbarossa Live'
    }
    return render(request, 'main/home.html', context)