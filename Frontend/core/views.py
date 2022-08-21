
from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
# Create your views here.
import datetime



from django.views import View
class MyView(View):
    template = 'index.html'
    def get(self, request):
        # <view logic>
        return render(request, self.template)

        return render(request, self.template, context)

        return HttpResponse('result')
    def post(self,request):
        name= request.POST.get("Name")
        desc= request.POST.get("Description")
        print(name,desc)
        return HttpResponse('result')

        pass

# from django.views.generic import TemplateView

# class AboutView(TemplateView):
#     template_name = "index.html"