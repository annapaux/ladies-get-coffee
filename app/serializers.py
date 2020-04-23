from rest_framework import serializers
from app.models import Company, University

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = ['name']

class IncredibleInputSerializer(serializers.Serializer):
    model_input = serializers.CharField()
