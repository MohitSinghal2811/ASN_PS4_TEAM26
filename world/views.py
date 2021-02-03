from django.shortcuts import render
from .load_anomalies import run
from django.http import HttpResponse
from .models import Anchors, RealTimeVessel, Trajectory, Anomaly, AnomalyDay1, AnomalyDay2, AnomalyDay3, AnomalyDay4, AnomalyDay6, Fishermen
from django.core.serializers import serialize
import json 
import math
import random
from django.db import connection
from datetime import datetime
import os

def anchors(request):
    countries = ["IND", "IDN", "THA", "MYS", "VNM", "BRN", "PHL", "MMR", "KHM", "SGP"]
    context = {"countries" : countries}
    return render(request, 'world/anchorageskgl.html', context=context)


def run_load(request):
    run()
    return HttpResponse({ "Loading done "})

def load_anchors(request, iso3):
    vars = serialize('geojson', Anchors.objects.filter(iso3 = iso3))
    return HttpResponse(vars, content_type= 'json')


def fishing_activity(request):
    f = open('colors.json')
    colors = json.load(f)
    print(colors)
    context = {"colors" : colors}
    return render(request, 'world/fishing_activity.html', context)

def track_vessel(request):
    return render(request, "world/tracker_vessel.html")


def load_driftinglonglines(request):
    vars = serialize('geojson', RealTimeVessel.objects.filter(geartype = "drifting_longlines"))
    print(vars)
    return HttpResponse(vars, content_type= 'json')

def load_fixedgear(request):
    vars = serialize('geojson', RealTimeVessel.objects.filter(geartype = "fixed_gear"))
    print("HI")
    return HttpResponse(vars, content_type= 'json')    

def load_squidjigger(request):
    vars = serialize('geojson', RealTimeVessel.objects.filter(geartype = "squid_jigger"))
    print("HI")
    return HttpResponse(vars, content_type= 'json')

def load_purseseines(request):
    vars = serialize('geojson', RealTimeVessel.objects.filter(geartype = "purse_seines"))
    print("HI")
    return HttpResponse(vars, content_type= 'json')

def load_trawlers(request):
    vars = serialize('geojson', RealTimeVessel.objects.filter(geartype = "trawlers"))
    print("HI")
    return HttpResponse(vars, content_type= 'json')

def load_others(request):
    vars = serialize('geojson', RealTimeVessel.objects.filter(geartype = "other_fishing"))
    print("HI")
    return HttpResponse(vars, content_type= 'json')


def utils(request):
    f = open('mids.json')
    data = json.load(f)
    colors = {}
    for d in data:
        color = getRandomColor()
        colors[d] = color

    colors = json.dumps(colors)
    with open('colors.json', 'w') as outfile:
        outfile.write(colors)
    return HttpResponse("HI")

def getRandomColor():
  letters = '0123456789ABCDEF'
  color = '#'
  for i in range(6):
    color += letters[math.floor(random.random() * 16)]
  return color

def load_tracks(request, mmsi, start , end):
    startstamp = datetime(datetime.strptime(start, '%Y-%m-%dT%H:%M').year, datetime.strptime(start, '%Y-%m-%dT%H:%M').month, datetime.strptime(start, '%Y-%m-%dT%H:%M').day, datetime.strptime(start, '%Y-%m-%dT%H:%M').hour, datetime.strptime(start, '%Y-%m-%dT%H:%M').minute).timestamp()
    endstamp = datetime(datetime.strptime(end, '%Y-%m-%dT%H:%M').year, datetime.strptime(end, '%Y-%m-%dT%H:%M').month, datetime.strptime(end, '%Y-%m-%dT%H:%M').day, datetime.strptime(end, '%Y-%m-%dT%H:%M').hour, datetime.strptime(end, '%Y-%m-%dT%H:%M').minute).timestamp()
    vars = serialize('geojson', Trajectory.objects.filter(mmsi = mmsi).filter(time__gte = startstamp).filter(time__lte = endstamp).order_by('time'))
    objs = json.loads(vars)
    with open("world/data/jsons/data_file.json", "w") as write_file:
        json.dump(objs, write_file)
    return HttpResponse(vars, content_type= 'json')

def test2(request):
    command1 = 'ogr2ogr -f "KML" "world/data/kmls/destination_data.kml" "world/data/jsons/data_file.json"'
    command2 = 'ogr2ogr -f "KML" "world/data/shps/destination_data.shp" "world/data/jsons/data_file.json"'
    command3 = 'ogr2ogr -f "KML" "world/data/csvs/destination_data.csv" "world/data/jsons/data_file.json"'
    os.system("cmd /c " + command1)
    os.system("cmd /c " + command2)
    os.system("cmd /c " + command3)
    return render(request, 'world/test2.html')

def home(request):
    return render(request,'world/home_page/dist/index.html')

def signup(request):
    return render(request, 'world/sign_up/dist/index.html')

def pricing(request):
    return render(request, 'world/pricing_plan/dist/index.html')

def tabs(request):
    return render(request, 'world/module_tabs/dist/index.html')

def anomalies(request):
    return render(request, 'world/our_anomalies.html')

def load_anomalies_day1(request):
    vars = serialize('geojson', AnomalyDay1.objects.all().order_by('datetime'))
    print(vars)    
    return HttpResponse(vars, content_type= 'json')

def load_anomalies_day2(request):
    vars = serialize('geojson', AnomalyDay2.objects.all().order_by('datetime'))
    print(vars)    
    return HttpResponse(vars, content_type= 'json')

def load_anomalies_day3(request):
    vars = serialize('geojson', AnomalyDay3.objects.all().order_by('datetime'))
    print(vars)    
    return HttpResponse(vars, content_type= 'json')

def load_anomalies_day4(request):
    vars = serialize('geojson', AnomalyDay4.objects.all().order_by('datetime'))
    print(vars)    
    return HttpResponse(vars, content_type= 'json')


def load_anomalies_day6(request):
    vars = serialize('geojson', AnomalyDay6.objects.all().order_by('datetime'))
    print(vars)
    return HttpResponse(vars, content_type= 'json')


def load_traffic(request, start, end):
    startstamp = datetime(datetime.strptime(start, '%Y-%m-%dT%H:%M').year, datetime.strptime(start, '%Y-%m-%dT%H:%M').month, datetime.strptime(start, '%Y-%m-%dT%H:%M').day, datetime.strptime(start, '%Y-%m-%dT%H:%M').hour, datetime.strptime(start, '%Y-%m-%dT%H:%M').minute).timestamp()
    endstamp = datetime(datetime.strptime(end, '%Y-%m-%dT%H:%M').year, datetime.strptime(end, '%Y-%m-%dT%H:%M').month, datetime.strptime(end, '%Y-%m-%dT%H:%M').day, datetime.strptime(end, '%Y-%m-%dT%H:%M').hour, datetime.strptime(end, '%Y-%m-%dT%H:%M').minute).timestamp()
    vars = serialize('geojson', Trajectory.objects.filter(time__gte = startstamp).filter(time__lte = endstamp).order_by('time'))
    objs = json.loads(vars)
    return HttpResponse(vars, content_type= 'json')

def sea_traffic(request):
    return render(request, 'world/sea_traffic.html')

def fishing_spots(request):
    return render(request, 'world/fishing_spots.html')



def nearby_fishing_spots(request):
    return render(request, 'world/nearby_fishing_spots.html')


def fishing_spots_pm(request):
    return render(request, 'world/fishing_activity_pm.html')


def fishermen(request):
    vars = Fishermen.objects.all()
    context = {'vars': vars}
    print(vars)
    return render(request, 'world/fishermen/index.html', context = context)






