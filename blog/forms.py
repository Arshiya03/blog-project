from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
