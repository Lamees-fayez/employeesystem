from django.db import models

def upload_employee_image(instance,file_name):
    extension=file_name.split('.')[1]
    return f'Employee/{instance}.{extension}'
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    salary = models.FloatField()
    image=models.ImageField()

    def __str__(self):
        return self.name
    