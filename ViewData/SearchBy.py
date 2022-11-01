import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Version1.settings') #导入django环境，方便测试
import django
django.setup()

from ViewData.models import *
from django.db.models.aggregates import Count



def SearchByDate(y1,m1,d1,y2,m2,d2):

    msg1 = y1+'-'+m1+'-'+d1
    msg2 = y2 + '-' + m2 + '-' + d2
    QuerySet = Data.objects.values('event_property_name').distinct()    #查询出所有的问题性质名称名称
    propertys = []
    for item in QuerySet:
        propertys.append(item.get('event_property_name'))                 #将查询结果存为

    dict_res={}
    data_of_propertys = []

    for property in propertys:
        data = Data.objects.filter(event_property_name = property,create_time__gte=msg1,create_time__lte = msg2).aggregate(total=Count('id'))
        num = data.get('total')
        data_of_propertys.append(num)
    dict_res.update({"数量":data_of_propertys})
    dict_res.update({"问题性质": propertys})

    return dict_res


def SearchByCommunity(y1,m1,d1,y2,m2,d2):
    msg1 = y1 + '-' + m1 + '-' + d1
    msg2 = y2 + '-' + m2 + '-' + d2
    QuerySet = Data.objects.values('community_name').distinct()    #查询出所有的问题性质名称名称
    hots = []
    for item in QuerySet:
        hots.append(item.get('community_name'))                 #将查询结果存为

    dict_res={}
    sum = 0
    for hot in hots:
        data = Data.objects.filter(community_name = hot,create_time__gte =msg1,create_time__lte =  msg2).aggregate(total=Count('id'))
        num = data.get('total')
        sum =sum +num
        dict_res.update({hot:num})

    return dict_res



def search2(y1,m1,d1,y2,m2,d2):
    msg1 = y1 + '-' + m1 + '-' + d1
    msg2 = y2 + '-' + m2 + '-' + d2
    # print(msg)
    QuerySet = Data.objects.values('street_name').distinct()    #查询出所有的街道名称
    QuerySet2 = Data.objects.values('event_type_name').distinct()     #查询出所有的小类名称
    streets = []
    main_types = []
    for item in QuerySet:
        streets.append(item.get('street_name'))                 #将查询结果存为列表
    for item in QuerySet2:
        main_types.append(item.get('event_type_name'))

    dict_res={}
    for main_type in main_types:
        data_of_main_type = []
        for street in streets:
            num = Data.objects.filter(street_name=street, create_time__gte=msg1,create_time__lte=msg2,
                                      event_type_name=main_type).aggregate(total=Count('id')).get('total')
            data_of_main_type.append(num)
        dict_res.update({main_type: data_of_main_type})
    dict_res.update({"街道名": streets})
    print(dict_res)
    return dict_res


def search4_month(given_month):
    msg = '2018-' + given_month
    QuerySet = Data.objects.values('event_type_name').distinct()  # 查询出所有的事件类型
    event_types = []
    for item in QuerySet:
        event_types.append(item.get('event_type_name'))                 #将查询结果存为列表

    dict_res = {}
    dict_res.update({'结办类型':['处置中','按期结办','超期结办']})

    sum1 = Data.objects.filter(intime_to_archive_num=1, create_time__startswith=msg).aggregate(total=Count('id')).get('total')
    sum2 = Data.objects.filter(intime_archive_num=1, create_time__startswith=msg).aggregate(total=Count('id')).get('total')
    sum3 = Data.objects.filter(overtime_archive_num=1, create_time__startswith=msg).aggregate(total=Count('id')).get('total')
    dict_res.update({'各事件总和':[sum1, sum2, sum3]})
    # 计算各事件的百分比
    for event_type in event_types:
        num1 = Data.objects.filter(intime_to_archive_num=1, create_time__startswith=msg, event_type_name=event_type).aggregate(
            total=Count('id')).get('total')
        num2 = Data.objects.filter(intime_archive_num=1, create_time__startswith=msg, event_type_name=event_type).aggregate(
            total=Count('id')).get('total')
        num3 = Data.objects.filter(overtime_archive_num=1, create_time__startswith=msg,event_type_name=event_type).aggregate(
            total=Count('id')).get('total')
        dict_res.update({event_type:[num1, num2, num3]})
    return dict_res


def search4_quarter(given_quarter):
    quarter_to_month = [['01','02','03'],['04','05','06'],['07','08','09'],['10','11','12']]
    QuerySet = Data.objects.values('event_type_name').distinct()  # 查询出所有的事件类型
    event_types = []
    for item in QuerySet:
        event_types.append(item.get('event_type_name'))  # 将查询结果存为列表

    dict_res = {}
    dict_res.update({'结办类型': ['处置中', '按期结办', '超期结办']})
    sum1, sum2, sum3 = 0, 0, 0
    for given_month in quarter_to_month[int(given_quarter)-1]:
        msg = '2018-' + given_month
        sum1 = sum1 + Data.objects.filter(intime_to_archive_num=1, create_time__startswith=msg).aggregate(total=Count('id')).get(
        'total')
        sum2 = sum2 + Data.objects.filter(intime_archive_num=1, create_time__startswith=msg).aggregate(total=Count('id')).get(
        'total')
        sum3 = sum3 + Data.objects.filter(overtime_archive_num=1, create_time__startswith=msg).aggregate(total=Count('id')).get(
        'total')
    dict_res.update({'各事件总和': [sum1, sum2, sum3]})
    # 计算各事件的百分比
    for event_type in event_types:
        num1, num2, num3 = 0, 0, 0
        for given_month in quarter_to_month[int(given_quarter)-1]:
            msg = '2018-' + given_month
            num1 = num1 + Data.objects.filter(intime_to_archive_num=1, create_time__startswith=msg,event_type_name=event_type).aggregate(total=Count('id')).get('total')
            num2 = num2 + Data.objects.filter(intime_archive_num=1, create_time__startswith=msg,event_type_name=event_type).aggregate(total=Count('id')).get('total')
            num3 = num3 + Data.objects.filter(overtime_archive_num=1, create_time__startswith=msg,event_type_name=event_type).aggregate(total=Count('id')).get('total')
        dict_res.update({event_type: [num1, num2, num3]})
    return dict_res


def search4_range(y1, m1, d1, y2, m2, d2):
    msg1 = y1 + '-' + m1 + '-' + d1
    msg2 = y2 + '-' + m2 + '-' + d2
    QuerySet = Data.objects.values('event_type_name').distinct()  # 查询出所有的事件类型
    event_types = []
    for item in QuerySet:
        event_types.append(item.get('event_type_name'))  # 将查询结果存为列表

    dict_res = {}
    dict_res.update({'结办类型': ['处置中', '按期结办', '超期结办']})
    sum1 = Data.objects.filter(intime_to_archive_num=1, create_time__gte=msg1, create_time__lte=msg2).aggregate(total=Count('id')).get(
        'total')
    sum2 = Data.objects.filter(intime_archive_num=1, create_time__gte=msg1, create_time__lte=msg2).aggregate(total=Count('id')).get(
        'total')
    sum3 = Data.objects.filter(overtime_archive_num=1, create_time__gte=msg1, create_time__lte=msg2).aggregate(total=Count('id')).get(
        'total')
    dict_res.update({'各类型总数':[sum1, sum2, sum3]})
    # 计算各事件的百分比
    for event_type in event_types:
        num1 = Data.objects.filter(intime_to_archive_num=1, create_time__gte=msg1, create_time__lte=msg2,
                                   event_type_name=event_type).aggregate(
            total=Count('id')).get('total')
        num2 = Data.objects.filter(intime_archive_num=1, create_time__gte=msg1, create_time__lte=msg2,
                                   event_type_name=event_type).aggregate(
            total=Count('id')).get('total')
        num3 = Data.objects.filter(overtime_archive_num=1, create_time__gte=msg1, create_time__lte=msg2,
                                   event_type_name=event_type).aggregate(
            total=Count('id')).get('total')
        dict_res.update({event_type:[num1, num2, num3]})
    return dict_res



if __name__ == '__main__':
    search2('2018','12','01','2018','12','01')