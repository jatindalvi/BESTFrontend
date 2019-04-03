from django.shortcuts import render
from website.models import EtimRawDataNew
from website.forms import RouteForm,StartForm,CostForm
import subprocess

# Create your views here.
RouteList=[]
RealRouteList=[]
StartList=[]
RealStartList=[]
output=None
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
        elif 'final_btn' in request.POST:
            list=RouteList+StartList
            print("list")
            #output=script_function(str(list))
            s="""SELECT * FROM `etim_raw_data_new` WHERE (routeNo="%d" OR routeNo="%d" OR routeNo="%d" OR routeNo="%d") AND (frmStopName="%s" OR frmStopName="%s" OR frmStopName="%s" OR frmStopName="%s")ORDER BY routeNo ASC"""
            print(s % tuple(list))
            #print(output)

    print(RealCost)
    context={
    'RealCost':RealCost,
    #'Output':output,
    }
    return render(request,'home.html',context=context)

def script_function( post_from_form):
    print(post_from_form)

    #return subprocess.check_call(['website/script.py',post_from_form])


def db(request):
    data=EtimRawDataNew.objects.all
    context={
    'data':data,
    }
    return render(request,'test.html',context=context)
