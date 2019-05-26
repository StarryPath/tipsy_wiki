# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from wiki.models import Column, Article, IMG, Comment, Team
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

# 主页


def index(request):
    columns = Column.objects.all()
    # 获取最新的五篇文章
    articles = Article.objects.all().order_by('-pub_date')[:5]

    # 获取最近的三条评论
    comments = Comment.objects.all().order_by('-pub_date')[:3]
    users = User.objects.all()
    teams = Team.objects.all()

    # user_key=User.objects.get(username=user_key)
    try:
        article = Article.objects.get(pk=10)
        context = {'columns': columns, 'articles': articles,
                   'article': article, 'users': users, 'teams': teams, 'comments': comments}
    except BaseException:
        context = {'columns': columns, 'articles': articles,
                   'users': users, 'teams': teams, 'comments': comments}
    return render(request, 'index.html', context)

# 介绍页面


def about(request):
    columns = Column.objects.all()
    context = {'columns': columns, }
    return render(request, 'wiki/about.html', context)

# 上传图片
@csrf_exempt
@login_required(login_url='wiki:index')
def upload(request):
    new_img = IMG(img=request.FILES['editormd-image-file'])
    new_img.save()
    url = new_img.img.url
    s = json.dumps({'success': 1, 'message': "aa", 'url': url})
    return HttpResponse(s)

# 注册


def register(request):
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']
    username = request.POST['username']
    if password2 == "" or username == "" or email == "":
        return HttpResponse(u"Input can not be empty!")
    else:
        if password2 == password1:
            try:
                User.objects.get(username=username)
                return HttpResponse(u"Username already exists")
            except BaseException:
                User.objects.create_user(username, email, password1)
                return HttpResponseRedirect(reverse('wiki:index'))

        else:
            return HttpResponse(u"Entered passwords differ!")

# 登录


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('wiki:user_page', args=[username]))
    else:
        return HttpResponse(u"login failure")

# 注销


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('wiki:index'))

# 用户中心
@login_required(login_url='wiki:index')
def user_page(request, user_key):
    columns = Column.objects.all()

    user_key = User.objects.get(username=user_key)
    group = User.objects.filter(team=user_key.team)
    list = []
    list.append(str(user_key.team))
    for person in group:
        list.append(str(person))
    num = len(list)
    context = {'columns': columns, 'user_key': user_key,
               'group': json.dumps(list), 'num': num}

    return render(request, 'wiki/user.html', context)

# 栏目页


def column_detail(request, column_slug):
    columns = Column.objects.all()
    column = Column.objects.get(slug=column_slug)

    contact_list = column.article_set.all()
    paginator = Paginator(contact_list, 9)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    context = {'column': column, 'columns': columns, 'contacts': contacts}
    return render(request, 'wiki/column.html', context)

# 文章详情页


def article_detail(request, column_slug, pk):
    columns = Column.objects.all()
    column = Column.objects.get(slug=column_slug)
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)

    context = {'article': article, 'columns': columns,
               'column': column, 'comments': comments}
    return render(request, 'wiki/article.html', context)


# 搜索


def search(request):
    title = request.POST.get('title')
    articles = Article.objects.filter(title__icontains=title)
    columns = Column.objects.all()
    context = {'articles': articles, 'columns':columns}
    return render(request, 'wiki/search.html', context)

# 评论


@login_required(login_url='wiki:index')
def article_comment(request):
    pk = request.POST.get('pk')
    comt_article = Article.objects.get(pk=pk)
    # comt_article=request.POST.get('comt_article')
    comt_author = User.objects.get(username=request.POST.get('comt_author'))
    comt_content = request.POST.get('comt_content')
    comment = Comment.objects.create(
        article=comt_article, author=comt_author, content=comt_content)
    return HttpResponseRedirect(comt_article.get_absolute_url())


# 编辑页面
@login_required(login_url='wiki:index')
def edit_page(request, pk):
    columns = Column.objects.all()
    if str(pk) == '0':
        context = {'columns': columns}
        return render(request, 'wiki/edit_page.html', context)
    article = Article.objects.get(pk=pk)
    if request.user.username != article.author.username:
        return HttpResponse(u'Sorry you cannot do that')
    context = {'article': article, 'columns': columns}
    return render(request, 'wiki/edit_page.html', context)

# 编辑页面提交
@login_required(login_url='wiki:index')
def edit_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    column = Column.objects.get(name=request.POST.get('column'))
    author = User.objects.get(username=request.POST.get('author'))
    pk = request.POST.get('pk', '0')
    if pk == '0':
        article = Article.objects.create(
            title=title, content=content, column=column, author=author)
        return HttpResponseRedirect(article.get_absolute_url())
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.column = column
    article.save()
    return HttpResponseRedirect(article.get_absolute_url())
