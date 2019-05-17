from django.contrib import admin
from .models import Column, Article, IMG, NewUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'home_display')

class IMGAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'pub_date', 'update_time')
    list_filter = ('column', 'author', 'pub_date')



class ProfileInline(admin.StackedInline):
    model = NewUser
    can_delete = False
    verbose_name_plural = "profile"

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(IMG, IMGAdmin)
