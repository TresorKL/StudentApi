from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    faculty = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
