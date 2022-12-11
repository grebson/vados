from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from .forms import ArticleForm
from .models import Article, Category


@login_required(login_url='login')
def index_view(request):
    articles = Article.objects.all()
    categories = Category.objects.all()

    context = {
        'articles': articles,
        'categories': categories,
    }

    return render(request, 'articles/index.html', context)


@login_required(login_url='login')
def create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()

            messages.success(request, _('Article has been created.'))
            return redirect('articles')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'articles/create.html', context)


@login_required(login_url='login')
def detail_view(request, pk):
    article = Article.objects.get(id=pk)

    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)


@login_required(login_url='login')
def update_view(request, pk):
    article = Article.objects.get(id=pk)

    if request.user != article.user:
        if request.user.is_superuser:
            pass
        else:
            messages.warning(request, _('You should not be here.'))
            return redirect('articles')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()

            messages.success(request, _('Article has been updated.'))
            return redirect('articles')
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request, 'articles/update.html', context)


@login_required(login_url='login')
def delete_view(request, pk):
    article = Article.objects.get(id=pk)

    if request.user != article.user:
        if request.user.is_superuser:
            pass
        else:
            messages.warning(request, _('You should not be here.'))
            return redirect('articles')

    if request.method == 'POST':
        article.delete()

        messages.success(request, _('Article has been deleted.'))
        return redirect('articles')

    context = {
        'article': article,
    }

    return render(request, 'articles/delete.html', context)


def category_view(request, pk):
    category = Category.objects.get(id=pk)
    articles = Article.objects.filter(category=category)
    categories = Category.objects.all()

    context = {
        'category': category,
        'articles': articles,
        'categories': categories,
    }

    return render(request, 'articles/category.html', context)
