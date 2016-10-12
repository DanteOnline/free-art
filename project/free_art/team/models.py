from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='team/developer')
    role = models.TextField(null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    linked_in_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    vk_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)


    def __str__(self):
        result = self.name
        if self.role:
            result += ' - ' + self.role
        return result

class Tester(models.Model):
    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='team/tester')
    mail = models.EmailField(null=True, blank=True)
    linked_in_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    vk_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    ref_url = models.URLField(null=True, blank=True)
    portfolio_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name