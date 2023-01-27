from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator 


def books_view(request):
    template = 'books/books_list.html'
    list_book = Book.objects.all()
    context = {'list_book': list_book}
    return render(request, template, context)

def book_date(request, pub_date):
    template = 'books/books_date.html'
    list_book_filt = Book.objects.filter(pub_date = pub_date)
    list_book = Book.objects.all()
    paginator = Paginator(list_book, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'list_book': page_obj, 'page': page_obj}
    return render(request, template, context)