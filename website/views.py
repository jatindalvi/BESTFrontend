from django.shortcuts import render
from website.models import EtimRawDataNew
from website.forms import RouteForm,StartForm,CostForm


# Create your views here.
RouteList=[]
RealRouteList=[]
StartList=[]
RealStartList=[]
def Home(request):
    RealRoute=0
    RealStart=0
    RealCost=0
    if request.method=="POST":
        if 'btnRoute_number' in request.POST:
            route_Number=RouteForm(request.POST)
            if route_Number.is_valid():
                RealRoute=route_Number.cleaned_data['route_number']
                RouteList.append(RealRoute)
        elif 'btnStart_name' in request.POST:
            start_Name=StartForm(request.POST)
            if start_Name.is_valid():
                RealStart=start_Name.cleaned_data['start_name']
                StartList.append(RealStart)
        elif 'btnCost_amount' in request.POST:
            cost_Amount=CostForm(request.POST)
            if cost_Amount.is_valid():
                print('abc')
                RealCost=cost_Amount.cleaned_data['cost_amount']
    print(RouteList)
    print(StartList)
    print(RealCost)
    context={
    'RealCost':RealCost,
    }
    return render(request,'home.html',context=context)


def db(request):
    data=EtimRawDataNew.objects.all
    context={
    'data':data,
    }
    return render(request,'test.html',context=context)
