from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SupersSerializer
from .models import Supers


"""
            ## address bar query logic ##
        dealership_name = request.query_params.get('dealership')
        print(dealership_name)

        queryset = Car.objects.all()

        if dealership_name:
            queryset = queryset.filter(dealership__name=dealership_name)
        
        
        ##original filter##
        # cars = Car.objects.all()
        serializer = CarSerializer(queryset, many=True) ##set first parameter to the correct object call function ['queryset' for filter, 'cars' for all]
        return Response(serializer.data)
    """


# Create your views here.
@api_view(['GET', 'POST'])

def supers_list(request):

    if request.method == 'GET':

        super_type = request.query_params.get('super_type')
        print(super_type)

        supers = Supers.objects.all()

        if super_type:
            supers = supers.filter(super_type__type=super_type)

        serialzer = SupersSerializer(supers, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
    
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