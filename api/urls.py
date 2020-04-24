from django.urls import include, path, re_path
from rest_framework import routers
from api import views
from django.conf.urls import url

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^incredible/$', views.IncredibleView.as_view()),
    url(r'^company/$', views.CompanyList.as_view()),
    url(r'^university/$', views.UniversityList.as_view()),
]
