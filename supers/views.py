from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SupersSerializer
from .models import Supers

# Create your views here.
@api_view(['GET', 'POST'])

def supers_list(request):

    if request.method == 'GET':
        
        supers = Supers.objects.all()
        serialzer = SupersSerializer(supers, many=True)
        return Response(serialzer.data)