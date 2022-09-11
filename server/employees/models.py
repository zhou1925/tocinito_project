from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=10)
    document_id = models.CharField(max_length=8)
    phone = models.CharField(max_length=9)
    birthday = models.DateField(null=True)
    address = models.CharField(max_length=20)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=20)
    employees = models.ManyToManyField(Employee, related_name="teams")

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
    
    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=20)
    employees = models.ManyToManyField(Employee, related_name="roles")

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name