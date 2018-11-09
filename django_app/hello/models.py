from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField(max_length=50)
    gender = models.BooleanField()
    age = models.IntegerField()
    birthday = models.DateField()

    def __str__(self):
        return '<Friend:id =' + str(self.id) + ', ' + self.name + '(' + str(self.age) + ')>'