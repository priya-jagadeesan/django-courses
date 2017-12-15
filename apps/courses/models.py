from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def get_dataValidator(self,postData):
        errors = {}
        try:
            if ( len(postData['name']) < 5) :
                errors ['name'] = "* Course name should be greater than 5 characters"

            if ( len(postData['desc']) < 15) :
                errors['desc'] = "* Give a course description of 15 characters or more"
        except:
            pass
        return errors


class Course(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Description(models.Model):
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    course = models.OneToOneField(Course)

class CommentManager(models.Manager):
    def get_dataValidator(self,postData):
        errors = {}
        try:
            if ( len(postData['ur_name']) <= 5) :
                errors ['ur_name'] = "* Please enter your name with atleast 5 characters"

            if ( len(postData['comment_text']) < 20) :
                errors['comment_text'] = "* Enter your commnents with more than 20 characters"
        except:
            pass
        return errors

class Comment(models.Model):
    name=models.CharField(max_length=255)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name="comments")
    objects = CommentManager()