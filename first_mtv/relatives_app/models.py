from django.db import models

# Create your models here.
class Family(models.Model):
    firstname=models.CharField (max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()
    birthday=models.DateField()

    def __str__(self) -> str:
        return f"{self.lastname} {self.firstname} {self.age} {self.birthday}"

