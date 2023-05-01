from django.db import models, connection

# Create your models here.


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @classmethod
    def get_title(cls, url):
        # Достаём название и юрл страниц, принадлежащих "главным"
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT title, url
                FROM menu_menuitem
                WHERE parent_id = (SELECT m1.id
                FROM menu_menuitem m1
                WHERE m1.url = %s)
            """, [url])
            row = cursor.fetchall()
            if len(row) != 0:
                items = {}
                iteration = 0
                for item in row:
                    iteration += 1
                    items[iteration] = {'title': item[0], 'url': item[1]}
                return items
            else:
                return None

    @classmethod
    def get_title_where_parent_null(cls):
        # Достаём "главные" страницы, которые ни к кому не привязаны
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT title, url
                FROM menu_menuitem
                WHERE parent_id is null
            """,)
            row = cursor.fetchall()
            if len(row) != 0:
                items = {}
                iteration = 0
                for item in row:
                    iteration += 1
                    print(f"itemitem {item}")
                    items[iteration] = {'title': item[0], 'url': item[1]}
                return items
            else:
                items = {1: {'title': 'Пожалуйста, добавьте страницы в админке', 'url': 'admin'}}
                return items
