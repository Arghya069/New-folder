from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from django.http.response import JsonResponse
from .models import Leds

# Create your views here.
def index(request,pk):
    led=Leds.objects.get(device_id=pk)
    data={"id":led.device_id,"led1":led.led1_status,"led2":led.led2_status,"led3":led.led3_status}
    return render(request,"index.html",data)

def A(request,pk):
    led=Leds.objects.get(device_id=pk)
    led.led1_status=1
    led.save()
    return redirect('index',pk)

def a(request,pk):
    led=Leds.objects.get(device_id=pk)
    led.led1_status=0
    led.save()
    return redirect('index',pk)

def B(request,pk):
    led=Leds.objects.get(device_id=pk)
    led.led2_status=1
    led.save()
    return redirect('index',pk)

def b(request,pk):
    led=Leds.objects.get(device_id=pk)
    led.led2_status=0
    led.save()
    return redirect('index',pk)

def C(request,pk):
    led=Leds.objects.get(device_id=pk)
    led.led3_status=1
    led.save()
    return redirect('index',pk)

def c(request,pk):
    led=Leds.objects.get(device_id=pk)
    led.led3_status=0
    led.save()
    return redirect('index',pk)

def Ldata(request,pk):
    led=Leds.objects.get(device_id=pk)
    return JsonResponse({'led1':str(led.led1_status),'led2':str(led.led2_status),'led3':str(led.led3_status)})