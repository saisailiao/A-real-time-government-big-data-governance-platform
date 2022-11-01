from django.contrib import admin
from Login import models

# Register your models here.
admin.site.site_header = '数据管理后台'
admin.site.site_title = '管理后台'
admin.site.register(models.User)