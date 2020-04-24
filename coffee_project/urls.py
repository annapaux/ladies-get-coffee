"""coffee_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# imported views
from app import views as app_views   # deleted to allow for more apps
# import authentication
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
# api
from django.urls import include
# messenger
from messenger import views as messenger_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # home
    url(r'^$', app_views.landing_page, name='landing_page'),
    # authentication
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # registration
    url(r'^signup/$', app_views.signup, name='signup'),
    # edit profile
    url(r'^edit_profile/$', app_views.edit_profile, name='edit_profile'),

    # API
    path('api/', include('api.urls')),

    # messenger
    url(r'^messages/$', messenger_views.view_messages, name='view_messages'),
    url(r'^messages/new_message$', messenger_views.send_message, name='send_message'),
]
