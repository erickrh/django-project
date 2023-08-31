from django import forms

class Create_new_task(forms.Form):
  title = forms.CharField(
    label='Title',
    max_length=200,
    widget=forms.TextInput(attrs={'class': 'input'})
  )
  
  description = forms.CharField(
    label='Description',
    widget=forms.Textarea(attrs={'class': 'input'}),
    required=False
  )
  
class Create_new_project(forms.Form):
  name = forms.CharField(
    label='Name',
    max_length=200,
    widget=forms.TextInput(attrs={'class': 'input'})
  )