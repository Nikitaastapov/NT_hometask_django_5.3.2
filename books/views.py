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
    paginator = Paginator(list_book_filt, 1)
    # sort_list = Book.objects.order_by('pub_date')
    
    previous_page = None 
    next_page = None
    def show_date(pub_date, next_page, previous_page):
        f_d = Book.objects.filter(pub_date__lt= pub_date).values('pub_date').first()
        if f_d.exists():
            previous_page = f_d
        n_d = Book.objects.filter(pub_date__gt=pub_date).values('pub_date').first()
        if n_d.exists():
            next_page = n_d
        
        
    
        
    

    context = {'list_book': paginator.object_list, 'page': {'up': next_page, 'down': previous_page}}
    return render(request, template, context)