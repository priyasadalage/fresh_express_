
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import action
from .serializers import*
from .models import *
from django.shortcuts import render,redirect
from django.http import HttpRequest
# Create your views here.

def home(request):
    bd=broadcast.objects.all()
    return render(request,'index.html',{'bd':bd})

    


class broadcastviewset(viewsets.ModelViewSet):
    queryset=broadcast.objects.all()
    serializer_class=broadcastSerializer

    def list(self,request):
        queryset=broadcast.objects.all()
        serializer_class=broadcastSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset=broadcast.objects.get(uid=id)
            serializer_class=broadcastSerializer(queryset)
            print(queryset.topic)
            return render(request,'oneBroadcast.html',{"uid":id,"bd":queryset})

    def create(self,request):
        serializer_class=broadcastSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return redirect('/')
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id=pk
        queryset=broadcast.objects.get(uid=id)
        serializer_class=broadcastSerializer(queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return redirect('/')
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        id =pk
        queryset=broadcast.objects.get(uid=id)
        serializer_class=broadcastSerializer(queryset, data=request.data,partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg':'Partial Data Updated','data':serializer_class.data})
        return Response(serializer_class.errors)



    def destroy(self, request, pk):
        id =pk
        queryset=broadcast.objects.get(uid=id)
        queryset.delete()
        return Response({'msg':'Data Deleted'})

def delete(request, uid):
    member = broadcast.objects.get(uid=uid)
    member.delete()
    return redirect('/')






    # redirect('home')
    
    

    
