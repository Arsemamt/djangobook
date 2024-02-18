from django.shortcuts import render,HttpResponse
from.models import  *

# Create your views here.

def home(request):
    info = CompanyInformation.objects.all().first()
    Books = Book.objects.all()

    data ={
        'info': info,
        'Books': Books
    }

    return render(request,'home.html',data) 

def about(request):
    return render(request,'about.html') 

def contact(request):
    return render(request,'contact.html') 

def book(request):
    return render(request,'book.html') 