#!/usr/bin/env python
# encoding: utf-8

"""
@author: lingxiangxinag 
@file: urls.py
@time: 2018/5/21 下午8:54

"""
from django.conf.urls import url

from python import views

urlpatterns = [
    url(r'^$', views.index),
]


