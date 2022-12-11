from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User


class Category(models.Model):
    name = models.CharField(_('name'), max_length=128, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=128, unique=True)
    content = models.TextField(_('content'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __str__(self):
        return self.title
