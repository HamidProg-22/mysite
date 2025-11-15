from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email')
    subject = forms.CharField(label='Subject', max_length=200)
    message = forms.CharField(label='Message', widget=forms.Textarea)