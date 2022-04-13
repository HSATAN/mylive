from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import datetime
# Create your models here.
# class User(models.Model):
#
#     username = models.CharField('用户名', max_length=20, unique=True)
#     password = models.CharField('用户密码',max_length=20)
#     #create_time = models.DateTimeField('创建时间', auto_now_add=True)
#     #change_password_time = models.DateTimeField('用户更改密码时间', auto_now=True)
#     #email = models.EmailField()
#     class Meta:
#         db_table = 'user'

class BlogUser(AbstractUser):
    nid = models.AutoField(primary_key = True)
    phone = models.CharField(max_length = 11)

    class Meta:
        db_table = 'blog_user'

class MyUser(models.Model):
    nick_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    userid = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    class Meta:
        db_table = 'myuser'

class Article(models.Model):
    article_body = models.TextField(max_length=5000)
    article_title = models.CharField(max_length=100)
    article_category = models.CharField(max_length=10)
    add_time = models.DateTimeField('添加时间', default=datetime.datetime.now())
    update_time = models.DateTimeField('更新时间', auto_now_add=True)
    owner_nid = models.ForeignKey(BlogUser, on_delete=models.CASCADE, unique=False)
    class Meta:
        db_table = 'blog_article'


