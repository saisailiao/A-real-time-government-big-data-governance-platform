from django.db.models import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .Uncompleted import *
import json

# Create your views here.
def alarm_view(request):
    res1 = FindUncompleted()
    #res2 = FindAlarm()
    #res = json.dumps(res, ensure_ascii=False)
    #return render(request, 'Alarm.html', {'msg_json': res})
    return render(request, 'Alarm.html',
                      {'uncompleted': json.dumps(res1),
                       #'alarm': json.dumps(res2),
                         })