from django import forms
from goplan.models import Project

class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'goplan','readonly':'readonly'}))
    class Meta:
        model = Project
        fields = ['name', 'repo']