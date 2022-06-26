from pickle import TRUE
from django.db import models
import re

class userManager(models.Manager):
    def basic_validator(self, postData,user = None):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters"
        elif len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        elif len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        elif postData['password'] != postData['confirm_pw']:
                errors['password'] = "Passwords DO NOT match!"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')   
        if not postData["email"]:
                errors["email"] = "Please enter email (Empty Check)"
        elif not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        else:
            # run the validation if we are in the process of creating a new user, or updating user
            if user is None or user.email != postData["email"]:
                if User.objects.filter(email=postData["email"]).exists():
                    errors["email"] = "The email is already exist, please try another one"
        return errors
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc=models.TextField()
    photo = models.ImageField(upload_to='', null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    role = models.CharField(max_length=255) #student or manager.
    course = models.ForeignKey(Course, related_name="users", on_delete=models.CASCADE, null=True)
    state = models.CharField(null= True, max_length=255)
    password = models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= userManager()

