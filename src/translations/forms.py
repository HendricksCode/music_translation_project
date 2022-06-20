from django import forms
from .models import Translate

class TranslateForm(forms.ModelForm):
    class Meta:
        model = Translate
        fields = [
            'english',
            'italian',
            'german',
            'french'
        ]

# class RawTranslateForm(forms.Form): started this on a lesson and decided not to do that lesson
#     english     = forms.CharField(max_length=120)
#     italian     = forms.CharField(max_length=120, blank=True, null=True)
#     german      = forms.CharField(max_length=120, blank=True, null=True)
#     french      = forms.CharField(max_length=120, blank=True, null=True)