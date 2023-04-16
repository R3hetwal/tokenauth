from django.db import models
from users.models import User
from ckeditor.fields import RichTextField
import uuid

# Create your models here.

class Project(models.Model):
    owner = models.ManyToManyField(User)
    project_name = models.CharField(max_length=255)
    description = models.TextField(null = True, blank = True)
    start_date = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name

class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_head = models.ForeignKey(User, on_delete=models.CASCADE, related_name='department_head', null=True)
    members = models.ManyToManyField(User)                                                                                                                                                                
    joined_date = models.DateTimeField(auto_now_add=True)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.department_name

class Document(models.Model):
    document_name = models.CharField(max_length=255, default='Document')
    project_name = models.ManyToManyField(Project)
    created_at = models.DateTimeField(auto_now_add=True)
    identifier = models.CharField(max_length=255, unique=True, default=uuid.uuid4, editable=False)
    content = models.TextField()

    def __str__(self):
        return self.document_name
