# Create Message
from django import forms
from messenger.models import Message

class MessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ['text']
