import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Version1.settings') #导入django环境，方便测试
import django
django.setup()

from ViewData.models import *
from django.db.models.aggregates import Count

def FindAlarm():
    msg = '2018-12-01'
    #uncompleted = Data.objects.filter(create_time__startswith=msg).aggregate(total=Count('id')).get('total')
    # uncompleted = Data.objects.filter(create_time__startswith=msg)
    uncompleted_1 = Data.objects.values('street_name').distinct()
    uncompleted_2 = Data.objects.values('sub_type_name').distinct()

    streets = []
    main_events = []
    for item in uncompleted_1:
        streets.append(item.get('street_name'))
    for item in uncompleted_2:
        main_events.append((item.get('sub_type_name')))

    record1 = {}
    dict_res_latest = []
    l_sorted_uncomplete = []
    for main_event in main_events:
        data_of_main_event = []
        for street in streets:
            num = Data.objects.filter(street_name=street, create_time=msg,
                                      sub_type_name=main_event).aggregate(total=Count('id')).get('total')
            items = Data.objects.filter(street_name=street, create_time=msg,
                                      sub_type_name=main_event)
            flag = 0
            for item in items:
                if(num >= 3 and flag ==0):
                   # print(street)
                    dict_res = {}
                    data_of_main_event.append(num)
                    dict_res.update({'统计时间': msg})
                    dict_res.update({"所属街道": street})
                    dict_res.update({'问题来源': item.event_src_name})
                    dict_res.update({'小类名称':main_event})
                    dict_res.update({'问题性质标识': item.event_property_name})
                    dict_res.update({'处置部门': item.dispose_unit_name})
                    dict_res.update({'反映次数': num})
                    dict_res_latest.append(dict_res)
                    flag = 1
    print(dict_res_latest)
    return dict_res_latest
    #sorted_uncompleted = uncompleted.order_by('event_type_id', 'rec_id')
    #print(sorted_uncompleted)
def FindUncompleted():
    msg = '2018-12-01'
    sorted_uncompleted = Data.objects.filter(create_time__startswith = msg)
    l_sorted_uncompleted = []
    #print(sorted_uncompleted)
    for item in sorted_uncompleted:
        record = {}
        record.update({'统计时间':item.create_time})
        record.update({'所属街道':item.street_name})
        record.update({'所属社区':item.community_name})
        record.update({'问题来源':item.event_src_name})
        record.update({'小类名称':item.sub_type_name})
        record.update({'问题性质标识':item.event_property_name})
        record.update({'处置部门':item.dispose_unit_name})
        l_sorted_uncompleted.append(record)
    print(l_sorted_uncompleted)
    return l_sorted_uncompleted

if __name__ == '__main__':
    FindUncompleted();
    FindAlarm();