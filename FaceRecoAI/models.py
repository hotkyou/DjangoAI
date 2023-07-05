from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Face(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='faces')
    def __str__(self):
        return self.person.name