from django import forms
from .models import Tokoh

class TokohForm(forms.ModelForm):
    class Meta:
        model = Tokoh
        fields = "__all__"
        