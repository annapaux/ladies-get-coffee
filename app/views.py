from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# registration
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# import model for view profiles
from django.contrib.auth.models import User

# edit profiles
from app.forms import EditProfile
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from app.models import UserProfile


def landing_page(request):
    if request.user.is_authenticated:
        profiles = UserProfile.objects.all()
        data = {'profiles':profiles}
        return render(request, "home.html", data)
    else:
        return render(request, "landing_page.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def edit_profile(request):
    '''
    If the user already edited the profile, then use that instance.
    Else, create a new entry.
    '''
    if UserProfile.objects.filter(user=request.user).exists():
        profile = UserProfile.objects.get(user=request.user)
    else:
        profile = None

    if request.method == 'POST':
        if profile:
            form = EditProfile(request.POST, instance=profile)
        else:
            form = EditProfile(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect('/edit_profile/')
        else:
            messages.error(request, 'Form not valid')
    else:
        if profile:
            form = EditProfile(instance=profile)
        else:
            form = EditProfile()
    return render(request, 'registration/edit_profile.html', {'form': form})
