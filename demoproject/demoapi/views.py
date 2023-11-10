from django.shortcuts import render
from .models import Data
from datetime import datetime
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#CREATE A MODEL SERIALIZER FOR THE DATA MODEL
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

    


#CREATE THE VIEWS
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def data_api(request, id=None):
    if request.method == 'GET':
        if id:
            #RETRIEVE A SINGLE RECORD
            data = Data.objects.filter(id=id).first()
            if not data:
                return Response({"detail": "Record not found"}, status=status.HTTP_404_NOT_FOUND )
            data = DataSerializer(data)
            return Response(data.data, status.HTTP_200_OK)
        else:
            #RETRIEVE ALL THE RECORDS 
            data = Data.objects.all()
            data = DataSerializer(data, many=True)
            return Response(data.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        #UPDATE A RECORD WHOSE "id" == id
        if id:
            data = Data.objects.filter(id=id).first()
            if not data:
                return Response({"detail": "Record not found"}, status=status.HTTP_404_NOT_FOUND )
            serializer = DataSerializer(data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        #ADD NEW RECORDS
        data = DataSerializer(data=request.data, many=isinstance(request.data, list))
        if data.is_valid():
            if isinstance(request.data, list):
                #CREATE MULTIPLE RECORDS AT ONCE   
                Data.objects.bulk_create([Data(**item_data) for item_data in data.validated_data])
            else:
                #CREATE A SINGLE RECORD
                Data.objects.create(**data.validated_data)
            return Response(data.data, status=status.HTTP_201_CREATED)
        print(data.errors)
        return Response({}, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # THE DELETE logic
        if id:
            data = Data.objects.filter(id=id).first()
            if not data:
                return Response({"detail": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
            data.delete()
            return Response({"detail": "Record deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
