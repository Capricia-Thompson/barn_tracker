from django.db import models

# Create your models here.


class ProgramManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least 2 characters."
        if postData['availability'] == "":
            errors['age'] = "Please enter an age."
        if len(postData['description']) < 8:
            errors['description'] = "Please enter a more detailed description."
        return errors


class Program(models.Model):
    name = models.CharField(max_length=100)
    availability = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProgramManager()
    image = models.ImageField(upload_to='program_pics/')
