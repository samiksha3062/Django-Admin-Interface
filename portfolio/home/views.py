from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'name':'Samiksha','course':'Django'}
    return render(request,'home.html',context)

def about(request):
    # return HttpResponse("This is my about page (/about)")
    return render(request,'about.html')

def projects(request):
    # return HttpResponse("This is my project page (/projects)")
    return render(request,'projects.html')

def concat(request):
    # return HttpResponse("This is my concat page (/concat)")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name,email,phone,desc)
        ins = Contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("Data has been retained to the DB")

    return render(request,'concat.html')




