from django.shortcuts import render
from website.models import EtimRawDataNew
# Create your views here.
def Home(request):
    return render(request,'home.html')
def db(request):
    data=EtimRawDataNew.objects.all
    context={
    'data':data,
    }
    return render(request,'test.html',context=context)
