from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.TextField(unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.question
