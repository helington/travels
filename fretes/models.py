from django.db import models

# Create your models here.


class Frete(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField()

    def makeDate(self):
        return f"{self.date.day}/{self.date.month}/{self.date.year}"

    def makeDateForHTML(self):
        return f"{self.date.year}-{self.date.strftime('%m')}-{self.date.day}"
        
    def __str__(self):
        return f"""
        id: {self.id}
        title: {self.title}
        date: {self.makeDate}
        """

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date.strftime("%b %d %Y, %I:%M %p")
        }