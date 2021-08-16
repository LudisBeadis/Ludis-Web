from django import forms
from .models import *

class messageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'