from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from supers.serializers import SuperSerializer


@api_view(['GET', 'POST']) 
def supers_list(request):

    supers = Super.objects.all()

    if request.method == 'GET':

        super_type_param = request.query_params.get('super_type') 
        
        if super_type_param == 'hero':
            supers = supers.filter(super_type__id=1) 
        elif super_type_param == 'villain':
            supers = supers.filter(super_type__id=2)
        else:
            supers = Super.objects.all()
        
        serializer = SuperSerializer(supers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE']) 
def super_detail(request,pk):

    super = get_object_or_404(Super,pk=pk)

    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status.HTTP_204_NO_CONTENT) 