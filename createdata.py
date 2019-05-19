# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from wiki.models import Column, Team, Article, Comment
User = get_user_model()

# 添加团队
teamlist = ['攻防技术组', '安全开发组', '数据挖掘组']
for teamname in teamlist:
    team = Team.objects.create(name=teamname)

# 添加超级用户
team = Team.objects.get(pk=1)
User.objects.create_superuser(
    username='admin', email='QQ@qq.com', password='admin', team=team)

# 添加其他用户
namelist1 = ['lintianxiang', 'liujiahaos', 'liyanzhe', 'zhangdachuan',

             'fuyao', 'jinzhen', 'zhangruiqi']

team = Team.objects.get(pk=1)
for name in namelist1:
    User.objects.create_user(
        username=name, email='123@123.com', password=name, team=team)


namelist2 = ['lihuaxin', 'lisirui', 'linjinxiu', 'huangxin',
             'wangxiaowei', 'wangyang']
team = Team.objects.get(pk=2)
for name in namelist2:
    User.objects.create_user(
        username=name, email='123@123.com', password=name, team=team)


namelist3 = ['yangjiageng', 'zhanghanwen', 'zhangzundong',
             'leipengqun', 'jiaozhengang', 'wangxuwu']
team = Team.objects.get(pk=3)
for name in namelist3:
    User.objects.create_user(
        username=name, email='123@123.com', password=name, team=team)


# 添加栏目
columnlist = ['CTF', 'WEB', 'PWN', 'REVERSE', 'WIKI']

for c_name in columnlist:
    column = Column.objects.create(name=c_name, slug=c_name)


# 添加文章
column = Column.objects.get(name='CTF')
author = User.objects.get(username='wangyang')
article = Article.objects.create(
    title='title1', content='content1', column=column, author=author)

column = Column.objects.get(name='WEB')
author = User.objects.get(username='huangxin')
article = Article.objects.create(
    title='title2', content='content2', column=column, author=author)

# 添加评论
article = Article.objects.get(pk=1)
author = User.objects.get(username='wangyang')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
