from django.db import models
import datetime
from ..log_reg.models import User
import re
import bcrypt

# Create your models here.


class CollectionManager(models.Manager):
    def collection_validator(self, postData):
        errors = {}
        if len(postData['collection_name']) < 5:
            errors['name'] = "Error, Name must be at least 5 characters."
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
    completed = models.BooleanField('completed', default=False)
    min_hours = models.PositiveIntegerField()
    max_hours = models.PositiveIntegerField()
    priority = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = AssignmentManager()
