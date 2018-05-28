# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return json.dump({"hello": "python"})
    return HttpResponse("python")