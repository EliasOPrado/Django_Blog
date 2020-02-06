from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#get the forms.py file
from . import forms
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})
    #eturn HttpResponse(slug)

@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == "POST":
        # need to pass both POST and FILES to submit files using CreateArticle function
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            '''
            On the code below the form will be save to the instance var
            then concatenated to the author (from the model) and request
            the same to the form. After that the instance will be saved.
            Basically adding a user = session['name'] to the form.
            '''
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})
