from django.conf.urls import url, include
from wiki import views as wiki_views



urlpatterns = [
    url(r'^$', wiki_views.index, name='index'),
    url(r'about/$', wiki_views.about, name='about'),
    url(r'^register/$',wiki_views.register,name='register'),
    url(r'^auth/$', wiki_views.auth, name='auth'),
    url(r'^logout/$', wiki_views.logout_view, name='logout'),
    url(r'^upload/$', wiki_views.upload, name='upload'),
    url(r'^user_page/(?P<user_key>[^/]+)/$', wiki_views.user_page, name='user_page'),
    url(r'^column/(?P<column_slug>[^/]+)/$', wiki_views.column_detail, name='column'),
    url(r'^article/(?P<column_slug>[^/]+)/(?P<pk>\d+)/$', wiki_views.article_detail, name='article'),
    url(r'^edit/(?P<pk>\d+)/$', wiki_views.edit_page, name='edit_page'),
    url(r'^edit/action/$', wiki_views.edit_action, name='edit_action'),
]