from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRgistrationFrom

def register_views(request):
    if request.method == 'POST':
        form = UserRgistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog_home') 
    else:
           form = UserRgistrationFrom()      
    return render(request, 'users/register.html', {'form': form})


def logo_views(request):
    messages.success(request, f'You have log out {username}!')
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_views(request):
    return render(request, "users/profile.html", {'title':'about'}, status=200)
