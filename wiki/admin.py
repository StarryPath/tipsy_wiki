from django.contrib import admin
from django.contrib.auth.models import User
from .models import Column, Article, IMG, UserExtension
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'home_display')

class IMGAdmin(admin.ModelAdmin):
    list_display = ('name', 'img')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'author', 'pub_date', 'update_time')
    list_filter = ('column', 'author', 'pub_date')

class EmployeeInline(admin.StackedInline):
    model = UserExtension
    verbose_name_plural = u'管理中心'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Column, ColumnAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(IMG, IMGAdmin)
