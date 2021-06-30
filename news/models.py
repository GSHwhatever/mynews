from django.db import models
import datetime
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField

# Create your models here.
from login.models import MyUser


class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = '新闻类别'
        verbose_name_plural = verbose_name


class Item(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    created_date = models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')
    completed = models.BooleanField(default=False, verbose_name='是否完成')
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = '新闻子栏目'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'名称')
    slug = models.SlugField(max_length=50, verbose_name=u'描述')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    slug = models.SlugField(unique_for_year='publish_data', verbose_name='描述')
    author = models.ForeignKey(MyUser, verbose_name='作者', on_delete=models.CASCADE)
    content = UEditorField(u'内容', height=400, width=600, default='', imagePath="upload/",
                           toolbars='mini', filePath='upload/', blank=True)
    status = models.CharField(max_length=2, verbose_name='状态')
    tags = models.ManyToManyField(Tag, blank=True)
    publish_data = models.DateTimeField(default=datetime.datetime.now(), verbose_name='发布日期')
    expiration_data = models.DateTimeField(blank=True, null=True, verbose_name='有效日期')
    is_active = models.BooleanField(default=True, blank=True, verbose_name='是否热门')
    pic = models.ImageField(upload_to='static/uploads', verbose_name='图片')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻文章'
        verbose_name_plural = verbose_name


class history(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    new = models.ForeignKey(News, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

