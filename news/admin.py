from django.contrib import admin
from .models import Category, Item, Tag, News, history


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fields = ['title']


class ItemAdmin(admin.ModelAdmin):
    fields = ['title', 'created_date', 'completed', 'news_category']


class TagAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']


class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'author', 'content', 'status', 'tags', 'publish_data', 'expiration_data', 'is_active', 'pic']

class historyAdmin(admin.ModelAdmin):
    fields = ['user', 'new']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(history, historyAdmin)

