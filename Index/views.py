from django.http import HttpResponse
from django.shortcuts import render
from Application import character as CRC
from Application import face_rec as FR
from Application import checkpicture as CP
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else: #POST:AIプログラム起動
        if request.POST.get('image') == '' or request.POST.get('picture') == '':
            data = {'error': '画像を選択してください。'}
            return Response(data, status=status.HTTP_411_LENGTH_REQUIRED)
        print(request.FILES['image'])
        image = request.FILES['image']
        picture = request.FILES['picture']
        Character = CRC.CharacterRec(image)
        if Character == None: #マイナンバーカードの文字が取得できない時
            data = {'error': '画像に影がかかっているか対応している身分証明書が選択されていません。'}
            return Response(data, status=status.HTTP_411_LENGTH_REQUIRED)
        FaceRec = FR.FaceRec(image, picture)
        if FaceRec == None: #身分証明書の顔が認識ができない時:
            data = {'error': '身分証明書の顔に影がかかっているか、見切れているため認識できませんでした。'}
            return Response(data, status=status.HTTP_411_LENGTH_REQUIRED)
        elif FaceRec == "": #現在の顔が認識できない時
            data = {'error': '現在の顔の画像に影がかかっているか、見切れているため認識できませんでした。'}
            return Response(data, status=status.HTTP_411_LENGTH_REQUIRED)
        #CheckPicture = CP.CheckPicture(image)
        #return render(request, 'index.html', {FR.FaceRec(image, picture)})
        data =  {'FaceRec': FaceRec, 
                'Character': Character, 
                #'CheckPicture': CheckPicture
                }
        #return HttpResponse(FaceRec, Character)
        return Response(data, status=status.HTTP_200_OK)