from django import forms


class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=25)
    mail = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
