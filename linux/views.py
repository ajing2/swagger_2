# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, status
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response

from linux.models import Linux
from linux.serializers import LinuxSerializer


class LinuxViewSet(viewsets.ModelViewSet):
    queryset = Linux.objects.all()
    serializer_class = LinuxSerializer

# @csrf_exempt
# def index(request):
#     # return json.dumps({"hello": "linux"})
#     print(request.method)
#     if request.method == 'GET':
#         return HttpResponse(json.dumps({"hello": "world_GET"}))
#     elif request.method == 'POST':
#         return HttpResponse(json.dumps({"hello": "world_POST"}))
#     else:
#         return HttpResponse(json.dumps({"hello": "world_other"}))
def test(request):
    return HttpResponse(json.dumps({"hello": "test"}))



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


from django.conf import settings

class LinuxList(generics.ListAPIView):
# class LinuxList(generics.ListCreateAPIView):
    serializer_class = LinuxSerializer
    queryset = Linux.objects.all()
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        page = int(request.GET["page"])
        page_size = int(request.GET["page_size"])
        # page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE")
        users = self.get_queryset()[(page-1)*page_size:page*page_size]
        print(users)
        serializer = LinuxSerializer(users, many=True)
        print("#############")
        # print(serializer.data)
        print("#############")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = LinuxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

