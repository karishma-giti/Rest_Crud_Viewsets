from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

class StudentViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_201_CREATED)

    def list(self,request):
        print('hii')
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        id=pk
        queryset = Student.objects.get(pk=id)
        serializer = StudentSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors,status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        id=pk
        queryset = Student.objects.get(pk=id)
        serializer = StudentSerializer(queryset,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        id=pk
        queryset = Student.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'data deleted'})







    

