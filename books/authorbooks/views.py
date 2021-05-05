from django.shortcuts import render, redirect
from .models import Author,Book
from .forms import *


# Create your views here.

def home(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    data = {"books":books,"authors":authors}
    authordata = {"authors":authors}
    return render(request, "authorbooks/home.html",data)


def create(request):
    authorform = AuthorForm()
    
    if(request.method=='POST'):
        form = AuthorForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")
    
    data = {"authorform":authorform}


    return render(request, "authorbooks/create.html",data)

def createbook(request):
    bookform = BookForm()
    
    if(request.method=='POST'):
        form = BookForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")
    
    data = {"bookform":bookform}


    return render(request, "authorbooks/createbook.html",data)

def deleteauthor(request,pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect("/")

def deletebook(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect("/")

def updateauthor(request,pk):
    author = Author.objects.get(id=pk)
    authorform = AuthorForm(instance=author)

    if(request.method=="POST"):
        form =  AuthorForm(request.POST, instance=author)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"authorform": authorform}
    return render(request, "authorbooks/updateauthor.html",data)

def updatebook(request,pk):
    book = Book.objects.get(id=pk)
    bookform = BookForm(instance=book)

    if(request.method=="POST"):
        form =  BookForm(request.POST, instance=book)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"bookform": bookform}
    return render(request, "authorbooks/updatebook.html",data)
