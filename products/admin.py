from django.contrib import admin
from .models import Product, Comment
from jalali_date.admin import ModelAdminJalaliMixin



class CommentTabular(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'active', 'stars', ]
    extra = 0


class AdminProduct(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ['title', 'price', 'datetime_created', 'active', ]

    inlines = [CommentTabular, ]


admin.site.register(Product, AdminProduct)


class AdminComment(admin.ModelAdmin):
    list_display = ['product', 'body', 'author', 'active', 'stars', 'datetime_create']


admin.site.register(Comment, AdminComment)
