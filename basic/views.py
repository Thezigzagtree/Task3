from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def dictback(response):
    a = {
        "HERE":"THERE",
        "WHERE":"?"
    }
    return JsonResponse(a)

def listback(response):
    b = [
        1,2,3,4,5
    ]
    return JsonResponse(b, safe=False)
