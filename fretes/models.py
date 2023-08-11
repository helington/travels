from django.db import models

# Create your models here.


class Frete(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField()

    def makeDate(self):
        return f"{self.date.day}/{self.date.month}/{self.date.year}"

    def makeDateForHTML(self):
        return f"{self.date.year}-{self.date.strftime('%m')}-{self.date.day}"

class Contato(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f"""
        id: {self.id}
        name: {self.name}
        phone_number: {self.phone_number}
        """