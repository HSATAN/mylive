# _*_ coding:utf-8 _*_
from django import forms
from django.contrib.auth.models import User
from blog.models import BlogUser, Article
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, widget=forms.TextInput(attrs={'placeholder': '用户名'}))
    password = forms.CharField(label='密码', min_length=6, max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'密码'}))
    #placeholder：输入框提示信息
class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='邮箱', min_length=3, widget=forms.EmailInput(attrs={
        'class': 'input', 'placeholder': '邮箱'}))
    password = forms.CharField(label='密码', min_length=6, max_length=20, widget=forms.PasswordInput(attrs={'placeholder':'密码'}))
    class Meta:
        model = BlogUser
        fields = ('username', 'password', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = BlogUser.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('该邮箱已经被注册')
        return email

class ArticleForm(forms.ModelForm):
    article_title = forms.CharField(label='文章标题', max_length=100,required=True)
    article_category = forms.CharField(label='文章类别', max_length=10, required=True)
    article_body = forms.CharField(widget=forms.Textarea, label="文章内容")
    class Meta:
        model = Article
        fields = ('article_title', 'article_category', 'article_body')