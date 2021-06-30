from django.contrib import admin
from .models import MyUser
# Register your models here.
class MyUserAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'email', 'state']


admin.site.register(MyUser, MyUserAdmin)

from django.contrib import admin

admin.site.site_header = '新闻后台管理系统'
admin.site.site_title = '新闻后台管理系统'
admin.site.index_title = '新闻后台管理系统'

