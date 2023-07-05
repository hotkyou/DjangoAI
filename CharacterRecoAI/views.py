from django.http import HttpResponse
from django.shortcuts import render

def request(request):
    if request.method == 'POST':
        if request.POST.get('image'):
            print(request.POST)
            response = HttpResponse(status=200)
            return response
        else:
            print('naiyo-')
        print(request.POST)
        return HttpResponse(request.POST)
    elif request.method == 'GET':
        print(request.GET)
        return HttpResponse(request.GET)