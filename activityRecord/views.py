from django.shortcuts import render
import json
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from django.utils import timezone
import datetime

@csrf_exempt    #忽略csrf检查，否则会报csrf错误
def index(request):
    branch_choice = (
        ('community', '社区党支部'),
        ('retired', '离退休老干部党支部'),
        ('company','非公企业联合党支部'),
    )
    data={'community':[0,0,0],'retired':[0,0,0],'company':[0,0,0],}
    Pobj=models.MemberInfo.objects.all()
    for p in Pobj:
        if p.post=="yubei":
            data[p.branch][1]+=1
        elif p.post!='qunzhong':
            data[p.branch][0] += 1
        data[p.branch][2] += 1

    return render(request,r"activityRecord/index.html",{'data':data})
