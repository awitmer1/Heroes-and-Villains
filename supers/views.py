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

        super_type = request.query_params.get('super_type')
        print(super_type)

        if super_type:
            supers = supers.filter(super_type__type=super_type)

        heroes_list = supers.filter(super_type__type="hero")
        villain_list = supers.filter(super_type__type="villain")

        serialzer = SupersSerializer(supers, many=True)
        hero_serializer = SupersSerializer(heroes_list, many=True)
        villain_serializer = SupersSerializer(villain_list, many=True)
        
        custom_response_dict = {
            'heroes': hero_serializer.data,
            'villains': villain_serializer.data
        }
        
        return Response(custom_response_dict, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':

        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])

def super_detail(request, pk):

    super = get_object_or_404(Supers, pk=pk)

    if request.method == 'GET':
        serializer = SupersSerializer(super);
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)