# from django.db import models


# # Create your models here;

# class Department(models.Model):
#      DepartmentId = models.AutoField(primary_key=True)
#      DepartmentName = models.CharField(max_length=500);

# class Employee(models.Model):
#      EmployeeId = models.AutoField(primary_key=True)
#      EmployeeName = models.CharField(max_length=500)
#      Department = models.CharField(max_length=500)
#      PhotoFileName = models.CharField(max_length=500)
#      DateOfJoining = models.DateField()


from django.db import models

class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

    def __str__(self):
        return self.DepartmentName

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    PhotoFileName = models.CharField(max_length=500)
    DateOfJoining = models.DateField()

    def __str__(self):
        return self.EmployeeName
