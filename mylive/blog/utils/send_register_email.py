# _*_ coding:utf-8 _*_
from django.core.mail import send_mail
import os
subject = '这是邮件主题'
message = '这是邮件信息'
from_email = '2237093983@qq.com'
recipient_email = ['2499090390@qq.com']
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylive.settings')
send_mail(subject,message,from_email,recipient_email)