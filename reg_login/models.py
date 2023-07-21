from django.db import models
import re
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First name must be at least 2 characters."
        if len(postData['lname']) < 2:
            errors['lname'] = "Last name must be at least 2 characters."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address."
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 characters."
        return errors


class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    dob = models.DateField()
    email = models.CharField(max_length=45)
    pw = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
