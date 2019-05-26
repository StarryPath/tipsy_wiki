# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Column, Article, IMG, Team, NewUser, Comment
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'home_display')


class IMGAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'intro')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'article')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'pub_date', 'update_time')
    list_filter = ('column', 'author', 'pub_date')


class UserAdmin(UserAdmin):
    # 重写fieldsets在admin后台加入自己新增的字段
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Teams'), {'fields': ('team',)}),
    )


admin.site.register(NewUser, UserAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(IMG, IMGAdmin)
