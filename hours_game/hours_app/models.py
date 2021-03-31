from django.db import models
import datetime
from datetime import datetime
import re, bcrypt
# Create your models here.
EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

# Create your models here.
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

class CollectionManager(models.Manager):
    def collection_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Error, Name must be at least 2 characters."
        if len(postData['description']) < 10:
            errors['description'] = "Error, Description must be more than 10 characters."
        return errors

        # if len(postData['travel_start']) < 0:
        #     errors['travel_dates'] = "Error, Trip start and end dates are required"
        # if len(postData['travel_end']) < 0:
        #     errors['travel_dates'] = "Error, Trip start and end dates are required"
        # now = datetime.now()
        # date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        # if datetime.strptime(postData['travel_start'], '%Y-%m-%d') < datetime.now():
        #     errors['travel_start'] = "Error, Start day must be in the future"
        # if postData['travel_start'] > postData['travel_end']:
        #     errors['travel_end'] = "Error, End day must be after the start day."
        return errors

class AssignmentManager(models.Manager):
    def assignment_validator(self, postData):
        errors = {}
        if len(postData['assignment_name']) < 5:
            errors['name'] = "Error, Name must be at least 5 characters."
        if len(postData['description']) < 10:
            errors['description'] = "Error, Description must be more than 10 characters."
        return errors


class Collection(models.Model):
    creator = models.ForeignKey(
        User, related_name='created_collections', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(max_length=100)
    completed = models.BooleanField('completed', default=False)
    priority = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CollectionManager()


class Assignment(models.Model):
    creator = models.ForeignKey(
        User, related_name='user_comments', on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, related_name="owns_assignments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField(max_length=100)
    completed = models.BooleanField('completed', null=False)
    min_hours = models.PositiveIntegerField()
    max_hours = models.PositiveIntegerField()
    priority = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AssignmentManager()



