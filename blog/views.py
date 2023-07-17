from django.shortcuts import render


def index(reguest):
    data = {
        'title': 'Главная страница'
    }
    return render(reguest, 'blog/index.html', data)


def about(reguest):
    data = {
        'title': 'Про нас'
    }
    return render(reguest, 'blog/about.html', data)

# def

