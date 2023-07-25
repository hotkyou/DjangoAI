from django.http import HttpResponse
from django.shortcuts import render
from Application import character
from Application import face_rec as FR
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def index(request):
    
    if request.method == 'GET':
        return render(request, 'index.html')
    
    else:
        if request.POST.get('image') == '' or request.POST.get('picture') == '':
            data = {'error': '画像を選択してください。'}
            return Response(data, status=status.HTTP_411_LENGTH_REQUIRED)
        
        image = request.FILES['image']
        picture = request.FILES['picture']
        
        CR = character.CreateAPI()
        FaceRec = FR.FaceRec(image, picture)
        Character = CR.main(image)
        
        data = {}
        data["FaceRec"] = FaceRec
        data["Character"] = Character
        
        return Response(data)