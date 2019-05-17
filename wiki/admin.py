from django.contrib import admin
from django.contrib.auth.models import User
from .models import Column, Article, IMG, UserExtension
from django.contrib.auth.admin import UserAdmin


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'home_display')

class IMGAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'pub_date', 'update_time')
    list_filter = ('column', 'author', 'pub_date')

class ProfileInline(admin.StackInlin):
    model = UserExtension
    can_delete = False
    verbose_name_plural = "extension"

class UserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(IMG, IMGAdmin)
