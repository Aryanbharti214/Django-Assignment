from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):

    # Q1
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    # Q2
    roll_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    # Q2
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='students'
    )

    # Q2
    class Meta:
        ordering = ['name']

    # Q1
    def __str__(self):
        return self.name