from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs=({"rows":10, "cols":80})))

    def log_data(self):
        print(self.cleaned_data.get('comment'))
