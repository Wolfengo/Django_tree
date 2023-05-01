from django import template
from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    # Передаём в HTML tag с ответом от базы данных
    current_item = MenuItem.get_title(menu_name)
    return current_item

