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
    else: #AIプログラム起動
        if request.POST.get('image') == '' or request.POST.get('picture') == '':
            data = {'error': 'Please select image'}
            return Response(data, status=status.HTTP_411_LENGTH_REQUIRED)
        print(request.FILES['image'])
        image = request.FILES['image']
        picture = request.FILES['picture']
        Character = CRC.CharacterRec(image)
        FaceRec = FR.FaceRec(image, picture)
        #CheckPicture = CP.CheckPicture(image)
        #return render(request, 'index.html', {FR.FaceRec(image, picture)})
        data =  {'FaceRec': FaceRec, 
                'Character': Character, 
                #'CheckPicture': CheckPicture
                }
        #return HttpResponse(FaceRec, Character)
        return Response(data, status=status.HTTP_200_OK)