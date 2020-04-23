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

# api (db)
from rest_framework import viewsets
from app.serializers import CompanySerializer, UniversitySerializer
from app.models import Company, University
from rest_framework import generics

# api (computation heavy)
from rest_framework.response import Response
from rest_framework import views
from app.serializers import IncredibleInputSerializer
import time, pickle
from app.tasks import incredible_distributed

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


# API (db)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

class CompanyList(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        starts_with = self.request.query_params.get('starts_with', None)
        if starts_with:
            queryset = Company.objects.filter(name__startswith=starts_with)
        else:
            queryset = Company.objects.all()
        return queryset


class UniversityViewSet(viewsets.ModelViewSet):
    # starts_with = self.request.query_params.get('starts_with')
    # queryset = University.objects.filter(name__startswith=starts_with)
    queryset = University.objects.all().order_by('name')
    serializer_class = UniversitySerializer


class UniversityList(generics.ListAPIView):
    serializer_class = UniversitySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        starts_with = self.request.query_params.get('starts_with', None)
        if starts_with:
            queryset = University.objects.filter(name__startswith=starts_with)
        else:
            queryset = University.objects.all()
        return queryset


# API (computation)
# https://stackoverflow.com/questions/27786308/django-and-rest-api-to-serve-calculation-based-requests

class IncredibleView(views.APIView):

    def get(self, request):
        # Validate the incoming input (provided through query parameters)
        serializer = IncredibleInputSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        # Get the model input
        data = serializer.validated_data
        model_input = data["model_input"]

        # VERSION 1: Perform the complex calculations
        # time.sleep(2)
        # complex_result = model_input + "xyz"

        # VERSION 2: CACHE & CONCURRENT OPERATIONS
        with open('app/incredible_cache.pickle', 'rb') as f:
            cache = pickle.load(f)
        if model_input in cache:
            complex_result = cache[model_input]
        # else compute it
        else:
            complex_result = incredible_distributed(model_input)
            cache[model_input] = complex_result
            with open('app/incredible_cache.pickle', 'wb') as f:
                pickle.dump(cache, f, pickle.HIGHEST_PROTOCOL)

        # Return it in your custom format
        return Response({
            "complex_result": complex_result,
        })
