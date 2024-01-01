from django import forms

class SentimentForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)


