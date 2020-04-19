# Edit Profile
from django import forms
from app.models import UserProfile

class EditProfile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'current_job']
