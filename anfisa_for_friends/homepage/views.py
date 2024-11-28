from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Запрос:
    ice_cream_list = IceCream.objects.values('title').exclude(is_published=False).filter(is_on_main=True)
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
