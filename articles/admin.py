from django.contrib import admin
from .models import Article
# Register your models here.

#import classes to admin (to show on admin)
admin.site.register(Article)
