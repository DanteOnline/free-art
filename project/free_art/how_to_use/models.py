from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def get_steps(self):
        return Step.objects.filter(subject=self)

    def __str__(self):
        return self.name

class Step(models.Model):
    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='how_to', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    subject = models.ForeignKey(Subject)

    def __str__(self):
        return '%d) %s'%(self.number,self.name)

    class Meta:
        ordering = ['number']





































