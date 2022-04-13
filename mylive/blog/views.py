from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from blog.models import User, BlogUser, Article
from django.contrib.auth.decorators import login_required
from blog.forms import LoginForm, RegisterForm, ArticleForm
from django.contrib.auth import authenticate, login
from django import forms
# Create your views here.

@login_required
def index(request):
    print(request.COOKIES)
    response = HttpResponse(render(request, 'blog/index.html'))
    #response.delete_cookie('sessionid')
    #print(response.cookies)
    return response

def register(request):
    print(type(request.user))
    print(request.user.nid)
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.email = form.clean_email()
            new_user.save()
            next_url = reverse('blog_login')
            print(next_url)
            return redirect(next_url)
    return render(request, 'blog/register.html', {'form': form})
def blog_login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        next_url = request.GET.get('next')
        print(username)
        print(password)
        print('’用户存在')

                # return HttpResponse('登陆成功')
        user = authenticate(request, username=username, password=password)
        if user:
                login(request, user=user)
                print("登录成功")
                if next_url is None:
                    next_url = '/'
                response = redirect(next_url)
                response.set_cookie('username', '',  max_age=-1)
                return response
        else:
            print('用户名或密码错误')
            return render(request, 'blog/login.html', {'form': form})

    else:
        return render(request, 'blog/login.html', {'form': form})

@login_required
def is_login(request):
    return render(request, 'blog/is_login.html')

@login_required
def add_article(request):
    """
    添加文章
    :param request:
    :return:
    """
    form = ArticleForm()
    if request.method == 'POST':
        nid = request.user.nid
        title = request.POST['article_title']
        body = request.POST['article_body']
        category = request.POST['article_category']
        print(nid,title,body,category)
        Article.objects.create(owner_nid_id = nid, article_title=title, article_category=category, article_body=body)
        return render(request, 'blog/article.html', {'form': form})
    else:
        form = ArticleForm()
        print(request.user.nid)
        return render(request, 'blog/article.html', {'form': form})