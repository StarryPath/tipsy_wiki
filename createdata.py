# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from wiki.models import Column
from wiki.models import Team
# 添加团队
teamlist = ['攻防技术组', '安全开发组', '数据挖掘组']
for team in teamlist:
    Team.objects.create(name=team)

i = 2
User = get_user_model()
User.objects.create_superuser(
    username='admin', email='QQ@qq.com', password='admin')
User.objects.filter(id=1).update(team='攻防技术组')
# 添加用户
namelist1 = ['lintianxiang', 'liujiahaos', 'liyanzhe', 'zhangdachuan',
             'fuyao', 'jinzhen', 'zhangruiqi']

for name in namelist1:
    User.objects.create_user(name, '123@123.com', name)
    User.objects.filter(id=i).update(team='攻防技术组')
    i = i+1

namelist2 = ['lihuaxin', 'lisirui', 'linjinxiu', 'huangxin',
             'wangxiaowei', 'wangyang']

for name in namelist2:
    User.objects.create_user(name, '123@123.com', name)
    User.objects.filter(id=i).update(team='安全开发组')
    i = i+1

namelist3 = ['yangjiageng', 'zhanghanwen', 'zhangzundong',
             'leipengqun', 'jiaozhengang', 'wangxuwu']

for name in namelist3:
    User.objects.create_user(name, '123@123.com', name)
    User.objects.filter(id=i).update(team='数据挖掘组')
    i = i+1


# 添加栏目
columnlist = ['CTF', 'WEB', 'PWN', 'REVERSE', 'WIKI']

for c_name in columnlist:
    column = Column.objects.create(name=c_name, slug=c_name)
