import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import Application.autochecksex as checksex

@csrf_exempt
def diagnose(request):
    if request.method == 'POST':
        
        datas = json.loads(request.body)
        ACSFJ = checksex.AutoCheckFromJSON()
        result = ACSFJ.autoCheck(datas)
        print(result)

        return JsonResponse(result, safe=False)
    
    else:
        
        return HttpResponse("ここをどこだと思っているんだあああ")