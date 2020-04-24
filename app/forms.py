# Edit Profile
from django import forms
from app.models import UserProfile
from api.models import Company, University

class EditProfile(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    university = forms.ModelChoiceField(queryset=University.objects.all())

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'current_job', 'company', 'university']
