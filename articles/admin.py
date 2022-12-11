from django.contrib import admin
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
