from django.contrib import admin
from .models import Post, Group

# При регистрации модели Post источником конфигурации для неё назначаем
# класс PostAdmin
class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    empty_value_display = '-пусто-'
    list_editable = ('group',)

# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'title', 'slug', 'description')
#     empty_value_display = '-пусто-'

admin.site.register(Post, PostAdmin)
admin.site.register(Group)
