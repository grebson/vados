from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Article, Category


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label=_('Title'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
    )
    content = forms.CharField(
        label=_('Content'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        }),
    )
    category = forms.ModelChoiceField(
        label=_('Category'),
        required=False,
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
    )

    class Meta:
        model = Article
        fields = ('title', 'content', 'category')
