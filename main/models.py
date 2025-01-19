from django.db import models

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    centre_no1 = models.CharField(max_length=50)
    centre_no2 = models.CharField(max_length=50)
    date = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.language} - {self.level}"
