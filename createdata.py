from django.contrib.auth.models import User
from wiki.models import Column

namelist = ['lintianxiang', 'jiaozhengang', 'liyanzhe', 'zhangdachuan',
            'fuyao', 'jinzhen', 'lihuaxin', 'lisirui', 'linjinxiu', 'huangxin',
            'wangxiaowei', 'wangyang', 'yangjiageng', 'zhanghanwen', 'zhangzundong',
            'leipengqun', 'liujiahao', 'wangxuwu']

#for name in namelist:
#    user = User.objects.create_user(name, '123@123.com', name)


columnlist=['CTF','WEB','PWN','REVERSE','WIKI']


for c_name in columnlist:
    Column = Column.objects.create(name=c_name, slug=c_name )