from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def signup_view(request):
    if request.method == "POST":
        # will post the user-data to the db
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # will save the user-data to the db
            form.save()
            #todo: log the user in
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})
