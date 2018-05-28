#!/usr/bin/env python
# encoding: utf-8

"""
@author: lingxiangxinag 
@file: serializers.py
@time: 2018/5/23 下午2:59

"""
from django.utils.timezone import now
from rest_framework import serializers
from linux.models import Linux


class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()


class LinuxSerializer(serializers.ModelSerializer):
    # days_since_created = serializers.SerializerMethodField()
    teacher = ToUpperCaseCharField()
    class Meta:
        model = Linux
        fields = '__all__'
        # fields = ('id', 'teacher', 'age')

    # def get_days_since_created(self, obj):
    #     return (now() - obj.created).days

