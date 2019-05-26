# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from wiki.models import Column, Team, Article, Comment
User = get_user_model()

# 添加团队


Team.objects.create(name='攻防技术组', intro='攻防技术组基于网络攻防技术、运用各种网络攻防工具、搜索操作系统的漏洞，对其进行加固或者攻击。熟练掌握目前包括Windows、Linux、移动终端上的主流的攻防手段、技术、工具等。积极主动地关注国内外最新安全攻防技术，制定符合实际需要的网络安全策略，防止可能从网络和系统内部或外部发起的攻击行为，重点防止那些来自具有敌意的国家、企事业单位、个人和内部恶意人员的攻击。')
Team.objects.create(name='安全开发组', intro='安全开发组主要负责安全业务系统开发，组织信息安全项目的规划咨询、售前支持、项目建设、系统运维；编写系统中的关键模块和关键算法的程序，并进行安全综合测试、修改、代码走查工作。同时负责系统的总体技术方案、系统设计和系统的质量控制。此外小组需对于web安全、服务端安全、客户端安全、移动安全、无线安全、物联网安全等有深入了解和研究，并且熟悉信息安全行业背景和市场现状及未来发展趋势，深度理解国家信息安全相关政策、制度、标准，并可灵活运用。')
Team.objects.create(name='数据挖掘组', intro='数据挖掘组的工作在于从大量的、不完全的、有噪声的、模糊的、随机的实际数据中，通过算法搜索和提取隐含其内的、人们实现所不知的，但又是有潜在价值的信息和知识，进行价值化的分析。通过统计、在线分析处理、情报检索、机器学习、专家系统和模式识别等诸多方法来实现上述目标。同时需要掌握其他领域的各种知识与技术，如：统计学的抽样、估计和假设检验；人工智能、模式识别和机器学习的搜索算法、建模技术和学习理论。')

# 添加超级用户
team = Team.objects.get(pk=1)
User.objects.create_superuser(
    username='admin', email='QQ@qq.com', password='admin', team=team)

# 添加其他用户
namelist1 = ['lintianxiang', 'liujiahaos', 'liyanzhe', 'zhangdachuan',

             'fuyao', 'jinzhen', 'zhangruiqi', 'liuyumeng']

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
author = User.objects.get(username='wangxuwu')
article = Article.objects.create(
    title='title2', content='content2', column=column, author=author)

column = Column.objects.get(name='REVERSE')
author = User.objects.get(username='huangxin')
article = Article.objects.create(
    title='title3', content='content2', column=column, author=author)

column = Column.objects.get(name='PWN')
author = User.objects.get(username='lisirui')
article = Article.objects.create(
    title='title4', content='content2', column=column, author=author)

column = Column.objects.get(name='WIKI')
author = User.objects.get(username='liuyumeng')
article = Article.objects.create(
    title='title5', content='content2', column=column, author=author)

# 添加评论
article = Article.objects.get(pk=1)
author = User.objects.get(username='wangyang')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')

article = Article.objects.get(pk=2)
author = User.objects.get(username='liuyumeng')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')
Comment.objects.create(article=article, author=author, content='认真评论,遵纪守法')



