from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    data = {
        'message': 'Welcome to the E-Commerce Store!'
    }
    return JsonResponse(data)
