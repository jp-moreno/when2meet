from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination

from .models import User
from .serializers import UserSerialiazer

# Create your views here.

class UserView(APIView, LimitOffsetPagination):
    def get(self, request, format=None):
        users = User.objects.all()
        results = self.paginate_queryset(users, request, view=self)
        serializer = UserSerialiazer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerialiazer(data=request.data)
        if "username" in request.data:
            users = User.objects.filter(username=request.data["username"])
            if(users):
                return Response(status=status.HTTP_409_CONFLICT)

        if serializer.is_valid():
            if "pic" in request.FILES:
                serializer.save(pic=request.FILES["pic"])
            else:
                serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)