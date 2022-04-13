from django.contrib import admin
from blog.models import User, BlogUser

# Register your models here.
admin.site.register(User)
admin.site.register(BlogUser)