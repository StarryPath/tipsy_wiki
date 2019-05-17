from django.contrib import admin
from .models import Column, Article, IMG, Team,NewUser
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'home_display')

class IMGAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'pub_date', 'update_time')
    list_filter = ('column', 'author', 'pub_date')


class NewUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(NewUser, NewUserAdmin)


# admin.site.unregister(User)
# admin.site.register(NewUser, UserAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(IMG, IMGAdmin)
