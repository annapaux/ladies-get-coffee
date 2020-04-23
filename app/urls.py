from django.urls import include, path, re_path
from rest_framework import routers
from app import views
from django.conf.urls import url

router = routers.DefaultRouter()
# router.register(r'company', views.CompanyViewSet)
# router.register(r'university', views.UniversityViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^incredible/$', views.IncredibleView.as_view()),
    # re_path(r'^company\?starts_with=[a-zA-Z]+/$', views.CompanyList.as_view()),
    url(r'^company/$', views.CompanyList.as_view()),
    url(r'^university/$', views.UniversityList.as_view()),
]
