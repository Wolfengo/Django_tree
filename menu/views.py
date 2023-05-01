from django.shortcuts import render
from .models import MenuItem

# Create your views here.


def menu(request, menu_name):
    current_url = request.path
    rep = current_url.replace('/', '')
    rep = rep.split('/')
    rep = list(filter(lambda x: x != '', rep))
    # Это было сделано для работы с "уровнями", чтобы, понимать от какого имени url нужно выгружать из базы данные
    if len(rep) == 1:
        return render(request, 'menu/menu.html', {'menu': rep[0]})
    elif len(rep) == 2:
        return render(request, 'menu/menu.html', {'menu': rep[-1]})


def home(request):
    current_item = MenuItem.get_title_where_parent_null()
    return render(request, 'menu/home.html', {'menu': current_item})
