import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Update

#def detail_view(request):
    #"""This will return json data"""
    #return render()
    #return HttpResponse(get_template().render({}))

def json_example_view(request):
    data = {
        'count':10000,
        'content':'some content'
    }
    json_data = json.dumps(data)
    #return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')
