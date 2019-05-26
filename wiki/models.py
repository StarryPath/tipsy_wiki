# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# 团队


class Team(models.Model):
    name = models.CharField('团队名称', max_length=256)
    intro = models.TextField('团队简介', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '团队'
        verbose_name_plural = '团队'
        ordering = ['name']

# 自定义的用户类


class NewUser(AbstractUser):
    team = models.ForeignKey(
        Team, default='', null=True, verbose_name='所属团队')
    # team = models.CharField('团队名称', max_length=256, null=True, blank=True)
# 栏目


class Column(models.Model):
    name = models.CharField('栏目名称', max_length=256)
    slug = models.CharField('栏目网址', max_length=256, db_index=True)
    intro = models.TextField('栏目简介', default='')
    home_display = models.BooleanField('首页显示', default=False)

    def get_absolute_url(self):
        return reverse('wiki:column', args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']  # 按照哪个顺序排序

# 文章


class Article(models.Model):
    column = models.ForeignKey(
        Column, default='', null=False, verbose_name='归属栏目')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='作者')

    title = models.CharField('标题', max_length=256)
    content = models.TextField()

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    published = models.BooleanField('正式发布', default=True)

    def get_absolute_url(self):
        return reverse('wiki:article', args=(self.column.slug, self.pk))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

# 评论


class Comment(models.Model):
    article = models.ForeignKey(
        Article, default='', null=False, verbose_name='文章')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='作者')
    content = models.TextField()
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

# 图片


class IMG(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='upload')
