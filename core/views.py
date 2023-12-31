from django.shortcuts import render
from django.http import HttpResponse
from .fcmmanager import sendPush
from .serializer import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from .models import AppUser
import requests
import datetime as DT
import time
from worker import worker
from apscheduler.schedulers.background import BackgroundScheduler as scheduler

from knox.models import AuthToken
from rest_framework.decorators import api_view
from rest_framework import status, permissions, generics
from rest_framework.response import Response 
from fcm_django.models import FCMDevice



BASE_URL = "https://lekbeshimun.gov.np/alerts"

# Create your views here.
## 
## 
##
_today = DT.date.today()+DT.timedelta(days=2)
_week_ago = _today - DT.timedelta(days=7)
today = str(_today)
lower = str(_week_ago)
t = today.split("-")
lo = lower.split("-")
q = "?created[min]="+lo[1]+"%2F"+lo[2]+"%2F"+lo[0]+"&created[max]="+t[1]+"%2F"+t[2]+"%2F"+t[0]
url  =  BASE_URL + q


def checkUpdate():
        response = requests.get(url,headers={'Connection':'close'})
        data = response.json()
        response.close()
        #print('xxx')
        if(len(data)>0):
          r =  sendPush()
          #print(r)
          pass
        

##Scheduler.

sch = scheduler()
sch.add_job(checkUpdate,'interval',seconds=30,max_instances=1)
sch.start()

    

def default(request):
    
   
    return HttpResponse('hello')


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({"user": UserSerializer(user,context = self.get_serializer_context()).data,
        "token":AuthToken.objects.create(user)[1]})

    
@api_view(['GET'])
def registerDevice(request):
    device=  FCMDevice()
    device.name='xx'
    device.active = True
    device.device_id='dd'
    device.registration_id = 'reg'
    device.type='mob'
    device.user_id = 1
    device.save()






@api_view(['GET'])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = AppUser.objects.get(username= request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response({"user":serializer.data})
    return Response({"error":serializer.errors})

@api_view(['GET'])
def feedsAll(request):
    q = 'articles-api'
    url = BASE_URL+q
    response = requests.get(url,headers={'Connection':'close'})
    data = response.json()
    response.close()
    return Response(data)


    