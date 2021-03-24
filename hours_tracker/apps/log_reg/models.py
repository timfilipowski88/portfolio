from django.db import models
from datetime import datetime
import re, bcrypt
# Create your models here.
EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        email_check = User.objects.filter(email_address=postData['email_address'])
        if len(postData['first_name']) < 2:
            errors['first_name'] = "Error, First Name must be longer than 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Error, Last Name must be longer than 2 characters."
        if len(postData['password']) < 8:
            errors['password'] = "Error Password must be longer than 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['password_match'] = "Error, your Passwords must match."
        if len(postData['email_address']) < 5:
            errors['email_short'] = "Error, Email must be longer than 4 characters."
        elif not EMAIL_REGEX.match(postData['email_address']):
            errors['email_valid'] = "Error, Please enter a valid email."
        elif email_check:
            errors['email_in_use'] = "Error, Email Address is already registered."
        return errors

    def login_validator(self, postData):
        errors = {}
        user_check = User.objects.filter(email_address=postData['email_address'])
        if not user_check:
            errors['please_register'] = "Error, Email not registered."
        else:
            if not bcrypt.checkpw(postData['password'].encode(), user_check[0].password.encode()):
                errors['password_wrong'] = "Error, Email and Password do not match."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=55)
    password = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

