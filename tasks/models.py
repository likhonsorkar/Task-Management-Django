from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
class Projects(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
class Tasks(models.Model):
    projects = models.ForeignKey(
        "Projects", on_delete=models.CASCADE, default=1
    )
    assing_to = models.ManyToManyField(Employee)
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TasksDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium') ,
        (LOW, 'Low') 
    )
    task = models.OneToOneField(Tasks, on_delete=models.CASCADE)
    assign_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
