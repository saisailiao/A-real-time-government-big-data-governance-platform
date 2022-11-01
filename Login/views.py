from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json

# Create your views here.


def login_view(request):
    method = request.method
    if method == 'GET':
        return render(request,'Login1.html')
    else:
        uname = request.POST.get('uname','')
        upwd = request.POST.get('upwd','')

        if uname and upwd:
            count = User.objects.filter(username=uname,userpwd=upwd).count()
            if count == 1:
                request.session['uname'] = uname            #将名字存入session域
                return render(request,'index1.html')
            return render(request,'Login1.html')


def logout_view(request):
    del request.session['uname']
    return render(request,'Login1.html')


def register(request):

    method = request.method
    res = " "
    if method == 'GET':
        print(res)
        res = json.dumps(res, ensure_ascii=False)
        return render(request, 'register.html', {"res1": res})

    else:
        uname = request.POST.get('uname', '')
        upwd = request.POST.get('upwd', '')
        invite_code = request.POST.get('code','')

        check = User.objects.filter(username=uname).count()
        count = Invite_code.objects.filter(invite_code=invite_code).count()


        if count == 1 and check ==0:
            User.objects.create(username=uname,userpwd=upwd)
            Invite_code.objects.filter(invite_code = invite_code).delete()
            return render(request, 'Login1.html', {"res1": res})

        elif count != 1:
            res = '邀请码有误'
            res = json.dumps(res,ensure_ascii=False)
            return render(request, 'register.html', {"res1": res})

        else:
            res = '用户名已存在'
            res = json.dumps(res, ensure_ascii=False)
            return render(request, 'register.html', {"res1": res})

