from django import forms
from cinema.models import cin

class cinform(forms.ModelForm):
    class Meta:
        model=cin
        fields='__all__'

