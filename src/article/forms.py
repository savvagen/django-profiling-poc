from django import forms
from .models import Article
from author.models import Author


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Subject"}))
    body = forms.CharField(label='', required=False,
                           widget=forms.Textarea(attrs={
                               "placeholder": "Set Body (Html or Text)",
                               "id": "art_body",
                               "class": "input-reset",
                               "rows": 10
                           }))
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Author:', widget=forms.Select())

    class Meta:
        model = Article
        fields = ["title", "subject", "body", "author"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "test" in title.lower():
            return title
        else:
            raise forms.ValidationError("Invalid: title should contain keyword 'test'")


class RawArticleForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Subject"}))
    body = forms.CharField(label='', required=False,
                           widget=forms.Textarea(attrs={
                               "placeholder": "Set Body (Html or Text)",
                               "id": "art_body",
                               "class": "input-reset",
                               "rows": 10
                           }))
    author = forms.IntegerField(label='Author:', widget=forms.NumberInput(attrs={"placeholder": "Set Author ID"}))
