from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
def index(request):
 # Генерация "количеств" некоторых главных объектов
 num_books = Book.objects.all().count()
 num_instances = BookInstance.objects.all().count()
 # Доступные книги (статус = 'На складе')
 # Здесь метод 'all()' применен по умолчанию.
 num_instances_available = BookInstance.objects.filter(status__exact=2).count()
 # Авторы книг,
 num_authors = Author.objects.count()
 # Отрисовка HTML-шаблона index.html с данными
 # внутри переменной context
 return render(request, 'index.html', context={
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'num_visits': num_visits
    })
class BookListView(generic.ListView):
 model = Book
class BookDetailView(generic.DetailView):
 model = Book
class BookListView(generic.ListView):
 model = Book
 paginate_by = 3
class AuthorListView(generic.ListView):
 model = Author
 paginate_by = 4

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
 """
 Универсальный класс представления списка книг,
 находящихся в заказе у текущего пользователя.
 """
 model = BookInstance
 template_name = 'catalog/bookinstance_list_borrowed_user.html'
 paginate_by = 10
 def get_queryset(self):
    return
BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')