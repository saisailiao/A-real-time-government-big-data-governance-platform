from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render
import re

class MidWareLogin(MiddlewareMixin):

    def process_request(self, request):
        pattern = re.compile(r'/admin.*?')
        item = re.search(pattern,request.path_info)
        key = request.session.get('uname', 0)
        url_list = ['/View/','/View/View1/','/View/View2/','/View/View3/','/View/View4/','/Alarm/']
        if request.path_info == '/Login/' or request.path_info == '/Login/Register/' or item!=None or request.path_info == '/Login/Logout/':
            return None
        elif key != 0 and request.path_info not in url_list:
            return render(request,'index1.html')
        elif key != 0 and request.path_info in url_list:
            return None
        else:
            print("this is new comer")
            return render(request,'Login1.html')