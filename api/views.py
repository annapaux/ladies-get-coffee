from django.shortcuts import render

# Create your views here.
# api (db)
from rest_framework import viewsets
from api.serializers import CompanySerializer, UniversitySerializer
from api.models import Company, University
from rest_framework import generics

# api (computation heavy)
from rest_framework.response import Response
from rest_framework import views
from api.serializers import IncredibleInputSerializer
import time, pickle
from api.tasks import incredible_distributed


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
