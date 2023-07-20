from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(reguest):
    news = Articles.objects.order_by('-date')
    return render(reguest, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'Articles'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'


def create(reguest):
    error = ''
    if reguest.method == 'POST':
        form = ArticlesForm(reguest.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(reguest, 'news/create.html', data)
