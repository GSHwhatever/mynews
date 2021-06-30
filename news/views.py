import math

from django.core.paginator import Paginator
from django.shortcuts import render, redirect


from login.models import MyUser
from news.models import News, Tag, history


def index(request):
    t_list = News.objects.filter(is_active=0).order_by('-publish_data')[:5]
    top_list = News.objects.filter(is_active=1).order_by('-publish_data')[:5]
    t1 = top_list[0]
    t2 = top_list[1]
    t3 = top_list[2]
    return render(request, 'index.html', {'top_list': top_list, "t_list": t_list, 't1':t1, 't2':t2, 't3':t3})


def detail(request, new_id):
    new = News.objects.filter(id=new_id)
    if  request.user.is_authenticated:
        i = request.user
        a = i.id
        id = MyUser.objects.get(id=a)
        history.objects.update_or_create(new=News.objects.get(id=new_id),user=id)
        return render(request, 'panorama.html', {"new": new})
    return render(request, 'panorama.html', {"new": new})


def find_new(request,num):
    key_value = request.GET.get("key_value", '')
    data = News.objects.filter(title__contains=key_value).order_by('-publish_data')
    if not len(data):
        data = False
        return render(request, 'find.html',{"data": data})
    pageObj = Paginator(data, 10)
    perPageList = pageObj.page(num)
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end + 1)
    return render(request, 'find.html', {"data": data,'currentNum':num,'postList':perPageList,'pageList':pageList})


def inlandnews(request,num):
    da = Tag.objects.get(slug='1')
    data = News.objects.filter(tags=da).order_by('-publish_data')
    if not len(data):
        data = False
        return render(request, 'inlandnews.html', {'data':data})
    # 创建分页器对象
    pageObj = Paginator(data, 10)
    # 获取当前页的数据
    perPageList = pageObj.page(num)
    # 生成页码数列表
    # 每页开始页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # 每页结束页码
    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end + 1)
    return render(request, 'inlandnews.html', {"data": data,'currentNum':num,'postList':perPageList,'pageList':pageList})


def outlandnews(request,num):
    da = Tag.objects.get(slug='2')
    data = News.objects.filter(tags=da).order_by('-publish_data')
    if not len(data):
        data = False
        return render(request, 'outlandnews.html', {'data':data})

    pageObj = Paginator(data, 10)
    perPageList = pageObj.page(num)
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end + 1)
    return render(request, 'outlandnews.html', {"data": data, 'currentNum':num,'postList':perPageList,'pageList':pageList})


def hotspotnews(request,num):
    da = Tag.objects.get(slug='3')
    data = News.objects.filter(tags=da).order_by('-publish_data')
    if not len(data):
        data = False
        return render(request, 'hotspotnews.html', {'data':data})

    pageObj = Paginator(data, 10)
    perPageList = pageObj.page(num)
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    end = begin + 9
    if end > pageObj.num_pages:
        end = pageObj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end + 1)
    return render(request, 'hotspotnews.html', {"data": data, 'currentNum':num,'postList':perPageList,'pageList':pageList})

