from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from author.models import Author
from authentication.views import get_current_user  
from django.urls import reverse

def authors_list(request):
    current_user = get_current_user(request)
    if not current_user or current_user.role != 1:
        return HttpResponse("Access denied. Librarians only.")
    authors = Author.get_all()
    return render(request, 'authors_list.html', {'authors': authors})

def author_create(request):
    current_user = get_current_user(request)
    if not current_user or current_user.role != 1:
        return HttpResponse("Access denied. Librarians only.")
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        if name and surname and patronymic:
            Author.create(name, surname, patronymic)
            return redirect(reverse('authors_list'))
        else:
            return HttpResponse("All fields are required.")
    return render(request, 'author_create.html')

def author_delete(request, author_id):
    current_user = get_current_user(request)
    if not current_user or current_user.role != 1:
        return HttpResponse("Access denied. Librarians only.")
    author = get_object_or_404(Author, id=author_id)
    if author.books.exists():
        return HttpResponse("Cannot delete author - author is attached to one or more books.")
    else:
        author.delete()
        return redirect(reverse('authors_list'))


