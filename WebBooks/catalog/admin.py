from django.contrib import admin
from.models import Author, Book, Genre, Language, Status, BookInstance
#admin.site.register(Author)
#admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
admin.site.register(BookInstance)
#Определения к классу администратор
class AuthorAdmin(admin.ModelAdmin):
    pass
# Зарегистрируйте класс admin с соответствующей моделью
admin.site.register(Author, AuthorAdmin)
#Регистрируем классы администратора для книг
@admin.register(Book)
#Регистрируем классы администратора для экземпляра книги
@admin.register(BookInstance)
class AuthorAdmin(admin.ModelAdmin):
 list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
class BookAdmin(admin.ModelAdmin):
 list_display = ('title', 'genre', 'language', 'display_author')
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
 list_display = ('title', 'genre', 'language', 'display_author')
 list_filter = ('genre', 'author')
 pass
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
 list_filter = ('book', 'status')
 fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')
 }),
 ('Статус и окончание его действия', {
 'fields': ('status', 'due_back')
 }),
 )

class AuthorAdmin(admin.ModelAdmin):
 list_display = ('last_name', 'first_name')
 fields = ['first_name', 'last_name',
 ('date_of_birth', 'date_of_death')]

 class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
 list_display = ('title', 'author', 'display_genre')
 inlines = [BookInstance]
