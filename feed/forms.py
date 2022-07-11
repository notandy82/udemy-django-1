from django import forms

class PostForm(forms.Form):
    """ notes explaining purpose of class """
    image = forms.FileField()
    text = forms.CharField()
