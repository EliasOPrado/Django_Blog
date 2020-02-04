from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    #author = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    #will show only max 50 characters on the body
    #using snippet instead of body on template
    def snippet(self):
        return self.body[:50] + "..."
