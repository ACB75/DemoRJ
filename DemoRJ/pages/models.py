from django.db import models


class Person(models.Model):
    # Fields
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True)

    # Methods
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email


class Registro(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    registro_inicio = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    registro_fin = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    propuesta_inicio = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    propuesta_fin = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # Methods
    def __str__(self):
        return self.person.email + " " + self.registro_inicio + " " + self.registro_fin + " " + self.propuesta_inicio + " " + self.propuesta_fin
