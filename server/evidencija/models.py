from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    LastName = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=20)
    PersonalId = models.CharField(max_length=11)

    def __str__(self):
        return self.LastName + self.FirstName + self.PersonalId


class PersonRole(models.Model):
    ProjectCode = models.CharField(max_length=11)
    PersonId = models.CharField(max_length=11)
    RoleId = models.CharField(max_length=11)
    AssignmentDate = models.CharField(max_length=11)

    def __str__(self):
        return self.AssignmentDate


class Project(models.Model):
    # ProjectCode = models.CharField(max_length=20)
    Name = models.CharField(max_length=20)
    Description = models.CharField(max_length=20)
    StartDate = models.CharField(max_length=20)
    EndDate =  models.CharField(max_length=20)

    def __str__(self):
        return self.Name + self.Description + self.StartDate + self.EndDate


class Role(models.Model):
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name