from django.contrib.auth import get_user_model
User = get_user_model()
from wiki.models import Column
from wiki.models import Team
 
#添加用户
namelist = ['lintianxiang', 'jiaozhengang', 'liyanzhe', 'zhangdachuan',
            'fuyao', 'jinzhen', 'lihuaxin', 'lisirui', 'linjinxiu', 'huangxin',
            'wangxiaowei', 'wangyang', 'yangjiageng', 'zhanghanwen', 'zhangzundong',
            'leipengqun', 'liujiahao', 'wangxuwu']

for name in namelist:
   user = User.objects.create_user(name, '123@123.com', name)

#添加栏目
columnlist=['CTF','WEB','PWN','REVERSE','WIKI']

for c_name in columnlist:
    column = Column.objects.create(name=c_name, slug=c_name )

#添加团队
teamlist=['CTF','WEB','PWN','REVERSE','WIKI']