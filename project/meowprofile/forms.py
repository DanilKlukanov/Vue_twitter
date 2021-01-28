from django import forms
from .models import MeowProfile


class MeowProfileForm(forms.ModelForm):
    class Meta:
        model = MeowProfile
        fields = ('avatar',)
