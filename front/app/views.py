from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
# Create your views here.
import datetime



def newproject(request):
    return render(request,'index.html')

def mend2(request):
    # datas=req
    # return JsonResponse({'data':datas})
    # print('hello')
    name= request.POST.get("Name")
    desc=request.POST.get("Desc")
    print(name,desc)
    return HttpResponse('ok')
