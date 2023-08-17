import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import Application.autochecksex as checksex

from .models import Answer, Checkans, Checklist, Format, List, Session, Site, Version

@csrf_exempt
def diagnose(request):
    if request.method == 'POST':
        print(request.POST["1"])
        print(request.POST)
        datas = {"0": int(request.POST["0"]), "1": int(request.POST["1"]), "2": int(request.POST["2"]), "3": int(request.POST["3"]), "4": int(request.POST["4"])}
        print(datas)
        #datas = json.loads(request.body)
        ACSFJ = checksex.AutoCheckFromJSON()
        result = ACSFJ.main(datas)
        return HttpResponse(result["correct"])
        #return JsonResponse(result, safe=False)
    
    else:
        questionAnswers = [] #問題の答えを格納するリスト
        questionFormats = [] #問題の形式を格納するリスト
        latestVersion = Version.objects.latest('vnow').pk #問題の最新のバージョンを取得
        
        Questions = List.objects.filter(versionpk=latestVersion) #そのバージョンの問題を取得(version=latestVersion)
        questionCount = Questions.__len__() #問題の数を取得
        for question in Questions:
            answers = Answer.objects.filter(listpk=question.listpk) #最新バージョンの問題の答えを取得
            questionAnswers.append(answers)
            questionFormats.append(question.formatpk)
        combined_data = zip(Questions, questionAnswers, questionFormats)
        context = {
            'combined_data': combined_data,
            'questionCount': questionCount,
        }
        return render(request, 'diagnose/index.html', context)