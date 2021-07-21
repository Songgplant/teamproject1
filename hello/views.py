import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from analysis.MyAnalysis import MyAnalysis


def home(request):
    return render(request, 'home.html')

def ages(request):
    ott = request.GET['ott']
    result = MyAnalysis().forage(ott)
    return HttpResponse(json.dumps(result), content_type='application/json')

def sp(request) :
    ott = request.GET['ott']
    # feature = request.GET['feature']
    # # print(feature)
    result = MyAnalysis().ImdbScatter(ott)
    print("result 성공")
    return HttpResponse(json.dumps(result), content_type='application/json')