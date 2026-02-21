from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # Simple hello world page
    return render(request, 'hello/index.html', {'message': 'hello, world'})


def greet(request, user):
    # Hello {user} page
    return render(request, 'hello/greet.html', {'user': user})
