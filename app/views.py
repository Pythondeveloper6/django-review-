from django.shortcuts import render
from .models import MyData

# Create your views here.
def list(request):
    x = MyData.objects.all()
    return render(request,'qq.html',{'y':x})


def detail(request,info):
    a = MyData.objects.get(id=info)
    return render(request,'rr.html',{'p':a})



def create(request):
    pass


def update(request):
    pass


def deletee(request):
    pass