from django.db.models import QuerySet
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from .SearchBy import *
import json

# Create your views here.
def index_view(request):
    #data = Data.objects.filter(street_id=101)
    #return render(request,'showall.html',{'data':data})
    return render(request,'index1.html')

def street_view(request):
    #1 按街道返回
    all=request.GET.get('in_total','')
    #yyyy-mm-dd
    start_in_total = request.GET.get('start_in_total', '')
    end_in_total = request.GET.get('end_in_total', '')
    y1 = start_in_total[0:4]
    m1 = start_in_total[5:7]
    d1 = start_in_total[8:]
    y2 = end_in_total[0:4]
    m2 = end_in_total[5:7]
    d2 = end_in_total[8:]

    if y1 == '' and m1 == '' and d1 == '' and y2 == '' and m2 == '' and d2 == '' :
        res = SearchByDate('2018', '12', '01','2018','12','31')
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：2018-12-01至2018-12-31'
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData1.html', {'msg_json': res,'date':Date})

    elif y1 != '' and m1 != '' and d1 != '' and y2 == '' and m2 == '' and d2 == '' :#"始"时间不为空
        res= SearchByDate(y1,m1,d1,y1,m1,d1)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：'+y1+'-'+m1+'-'+d1
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request,'ViewData1.html',{'msg_json':res,'date':Date})

    elif y2 != '' and m2 != '' and d2 != '' and y1 == '' and m1 == '' and d1 == '' :#"末"时间不为空
        res= SearchByDate(y2,m2,d2,y2,m2,d2)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：'+y2+'-'+m2+'-'+d2
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request,'ViewData1.html',{'msg_json':res,'date':Date})
    else:
        res = SearchByDate(y1, m1, d1, y2, m2, d2)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：' + y1 + '-' + m1 + '-' + d1 + '至' + y2 + '-' + m2 + '-' + d2
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData1.html', {'msg_json': res, 'date': Date})


def hot_community(request):
    all = request.GET.get('in_total', '')
    # yyyy-mm-dd
    year = all[0:4]
    month = all[5:7]
    day = all[8:]
    print(all)
    if year == '' and month == ''and day == '':
        res= SearchByCommunity('2018','12','01')
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：2018-12-01'
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request,'ViewData3.html',{'msg_json':res,'date':Date})

    else:
        res= SearchByCommunity(year,month,day)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：' + year + '-' + month + '-' + day
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request,'ViewData3.html',{'msg_json':res,'date':Date})

def street_view2(request):
    all = request.GET.get('in_total', '')
    # yyyy-mm-dd
    start = request.GET.get('start_in_total', '')
    end = request.GET.get('end_in_total', '')
    y1 = start[0:4]
    m1 = start[5:7]
    d1 = start[8:]
    y2 = end[0:4]
    m2 = end[5:7]
    d2 = end[8:]

    if y1 == '' and m1 == '' and d1 == '' and y2 == '' and m2 == '' and d2 == '':
        res = search2('2018', '12', '01', '2018', '12', '31')
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：2018-12-01至2018-12-31'
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData2.html', {'msg_json': res, 'date': Date})

    elif y1 != '' and m1 != '' and d1 != '' and y2 == '' and m2 == '' and d2 == '':  # "始"时间不为空
        res = search2(y1, m1, d1, y1, m1, d1)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：' + y1 + '-' + m1 + '-' + d1
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData2.html', {'msg_json': res, 'date': Date})

    elif y2 != '' and m2 != '' and d2 != '' and y1 == '' and m1 == '' and d1 == '':  # "末"时间不为空
        res = search2(y2, m2, d2, y2, m2, d2)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：' + y2 + '-' + m2 + '-' + d2
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData2.html', {'msg_json': res, 'date': Date})
    else:
        res = search2(y1, m1, d1, y2, m2, d2)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：' + y1 + '-' + m1 + '-' + d1 + '至' + y2 + '-' + m2 + '-' + d2
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData2.html', {'msg_json': res, 'date': Date})


def handle_view(request):

    given_month_raw = request.GET.get('given_month', '')
    given_month=given_month_raw[5:7]
    given_quarter = request.GET.get('given_quarter', '')

    start = request.GET.get('start', '')
    end = request.GET.get('end', '')
    y1 = start[0:4]
    m1 = start[5:7]
    d1 = start[8:]
    y2 = end[0:4]
    m2 = end[5:7]
    d2 = end[8:]

    if y1 == '' and m1 == '' and d1 == '' and y2 == '' and m2 == '' and d2 == '' and given_month == '' and given_quarter == '':
        res = search4_range('2018', '12', '01', '2018', '12', '31')
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：2018-12-01至2018-12-31'
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData4.html', {'msg_json': res,'date':Date})
    elif given_month != '':
        res = search4_month(given_month)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：'+given_month
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData4.html', {'msg_json': res,'date':Date})
    elif given_quarter != '':
        res = search4_quarter(given_quarter)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：'+given_quarter
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData4.html', {'msg_json': res,'date':Date})
    else:
        res = search4_range(y1, m1, d1, y2, m2, d2)
        res = json.dumps(res, ensure_ascii=False)
        Date = '查询时间：'+y1+'-'+m1+'-'+d1+'至'+y2+'-'+m2+'-'+d2
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData4.html', {'msg_json': res,'date':Date})

def hot_community_baidu(request):
    #all = request.POST.get('in_total', '')
    start = request.GET.get('start_in_total', '')
    end = request.GET.get('end_in_total', '')
    y1 = start[0:4]
    m1 = start[5:7]
    d1 = start[8:]
    y2 = end[0:4]
    m2 = end[5:7]
    d2 = end[8:]
    print("test:")
    print(start)
    print(end)
    print(y1,m1,d1,y2,m2,d2)

    if y1 == '' and m1 == '' and d1 == '' and y2 == '' and m2 == '' and d2 == '':
        hot = SearchByCommunity('2018','12','01','2018','12','31')
        address_point = address_info.objects.all()
        address_longitude = []
        address_latitude = []
        address_data = []
        address_hot = []
        for i in range(len(address_point)):
            address_longitude.append(address_point[i].longitude)
            address_latitude.append(address_point[i].latitude)
            address_data.append(address_point[i].data)
            address_hot.append(hot.get(address_point[i].data))
        address_hot = json.dumps(address_hot)
        Date = '查询时间：2018-12-01至2018-12-31'
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData3.html',
                      {'address_longitude': json.dumps(address_longitude),
                       'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data),
                       'address_hot': address_hot, 'date': Date})

    elif y1 != '' and m1 != '' and d1 != '' and y2 == '' and m2 == '' and d2 == '':  # "始"时间不为空
        hot = SearchByCommunity(y1, m1, d1, y1, m1, d1)
        address_point = address_info.objects.all()
        address_longitude = []
        address_latitude = []
        address_data = []
        address_hot = []
        for i in range(len(address_point)):
            address_longitude.append(address_point[i].longitude)
            address_latitude.append(address_point[i].latitude)
            address_data.append(address_point[i].data)
            address_hot.append(hot.get(address_point[i].data))
        address_hot = json.dumps(address_hot)
        Date = '查询时间：' + y1 + '-' + m1 + '-' + d1
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData3.html',
                      {'address_longitude': json.dumps(address_longitude),
                       'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data),
                       'address_hot': address_hot, 'date': Date})

    elif y2 != '' and m2 != '' and d2 != '' and y1 == '' and m1 == '' and d1 == '':  # "末"时间不为空
        hot = SearchByCommunity(y2, m2, d2, y2, m2, d2)
        address_point = address_info.objects.all()
        address_longitude = []
        address_latitude = []
        address_data = []
        address_hot = []
        for i in range(len(address_point)):
            address_longitude.append(address_point[i].longitude)
            address_latitude.append(address_point[i].latitude)
            address_data.append(address_point[i].data)
            address_hot.append(hot.get(address_point[i].data))
        address_hot = json.dumps(address_hot)
        Date = '查询时间：' + y2 + '-' + m2 + '-' + d2
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData3.html',
                      {'address_longitude': json.dumps(address_longitude),
                       'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data),
                       'address_hot': address_hot, 'date': Date})

    else:
        hot = SearchByCommunity(y1, m1, d1, y2, m2, d2)
        address_point = address_info.objects.all()
        address_longitude = []
        address_latitude = []
        address_data = []
        address_hot = []
        for i in range(len(address_point)):
            address_longitude.append(address_point[i].longitude)
            address_latitude.append(address_point[i].latitude)
            address_data.append(address_point[i].data)
            address_hot.append(hot.get(address_point[i].data))
        address_hot = json.dumps(address_hot)
        Date = '查询时间：' + y1 + '-' + m1 + '-' + d1 + '至' + y2 + '-' + m2 + '-' + d2
        Date = json.dumps(Date, ensure_ascii=False)
        return render(request, 'ViewData3.html',
                      {'address_longitude': json.dumps(address_longitude),
                       'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data),
                       'address_hot': address_hot, 'date': Date})
