from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books/index.html', context)

def addBook(request):
    if request.method == 'POST':
        #add book
        return redirect('books:index')
    else:
        return redirect('books:index')

def addAuthor(request):
    if request.method == 'POST':
        #add author
        Author.objects.create(name=request.POST['name'])
        return redirect('books:index')
    else:
        return redirect('books:index')