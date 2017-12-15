from django.shortcuts import render,redirect,HttpResponse
from .models import *

# Create your views here.

def index(request):
    courses = Course.objects.all()
    data = { 'courses' : courses }
    return render(request,"courses/index.html",data)

def add(request):
    errors = Course.objects.get_dataValidator(request.POST)
    if len(errors) > 0:
        data = { 
            "errors" : errors,
            "courses" : Course.objects.all() 
        }
        return render(request,"courses/index.html",data)
    else:
        course = Course.objects.create(name=request.POST['name'])
        Description.objects.create(content=request.POST['desc'],course=course)
        return redirect(index)

def destroy(request,id):
    courses = Course.objects.filter(id=id)
    if len(courses) > 0:
        course = Course.objects.get(id=id)
        data = { "course" : course }
        return render(request,"courses/destroy.html",data)
    else:
        return redirect(index)

def destroyId(request,id):
    courses = Course.objects.filter(id=id)
    if len(courses) > 0:
        course = Course.objects.get(id=id)
        desc = Description.objects.filter(id=course.description.id)
        if len(desc) > 0:
            desc.delete()
        course.delete()
        return redirect(index)
    else:
        return redirect(index)

def comments(request,id):
    courses = Course.objects.filter(id=id)
    if len(courses) > 0:
        course = Course.objects.get(id=id)
    else:
        return redirect(index)
    comments = Comment.objects.filter(course=course)
    data = { "course" : course, 
            "comments" : comments
            }
    return render(request,"courses/comments.html",data)

def addComment(request,id):
    courses = Course.objects.filter(id=id)
    if len(courses) > 0:
        course = Course.objects.get(id=id)
    comments = Comment.objects.filter(course=course)
    data = {"course" : course,
            "comments" : comments
        }
    errors = Comment.objects.get_dataValidator(request.POST)
    if len(errors) > 0:
        data ['errors'] = errors
        return render(request,"courses/comments.html",data)
    else:
        comment = Comment.objects.create(name=request.POST['ur_name'],content=request.POST['comment_text'],course=course)    
        return render(request,"courses/comments.html",data)