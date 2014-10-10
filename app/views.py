from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import ApiKeySerializer,CoordsSerializer
from models import ApiKey,Coords
import json
# Create your views here.
class ApiKeyView(APIView):
    def post(self,request):
        try:
            key = request.DATA['key']
        except Exception as e:
            return Response(status=status.HTTP_204_NO_CONTENT)
        try:
            api_keys = ApiKey.objects.get(api_key=key)
            serializer = ApiKeySerializer(api_keys)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ApiKey.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
class CoordsView(APIView):
    def post(self,request):
        try:
            data = request.DATA    
            api = ApiKey.objects.get(api_key=data['api_key'])
            coords = Coords()    
            coords.user_api = api
            coords.message = data['message']
            coords.state = data['state']
            coords.coords = json.dumps(data['coords'])
            coords.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_204_NO_CONTENT)
            
            
        
    
        
        
        