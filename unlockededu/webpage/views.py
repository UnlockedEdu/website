from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def terms_and_conditions(request):
    return render(request, 'terms-and-conditions.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})


def about(request):
    return render(request, 'about.html', {})
