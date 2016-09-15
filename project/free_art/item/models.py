from django.db import models
from django_comments.moderation import CommentModerator, moderator
from django.core.urlresolvers import reverse
from django_comments.models import Comment

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    short_desc = models.TextField()
    full_desc = models.TextField(null=True, blank=True)
    def get_full_desc(self):
        if self.full_desc:
            return self.full_desc
        else:
            return self.short_desc

    image = models.ImageField(upload_to='category/main', null=True, blank=True)

    def has_image(self):
        if self.image:
            return True
        else:
            return False

    parent = models.ForeignKey('self',null=True,blank=True)

    @staticmethod
    def get_top_list():
        return Category.objects.filter(parent__isnull = True)

    def get_items(self):
        items = []
        if self.is_leaf():
            items = Script.objects.filter(category=self)
        else:
            children = self.get_children()
            for c in children:
                items.extend(c.get_items())
        return items

    def __str__(self):
        return self.name

    def has_parent(self):
        return self.parent != None

    def is_top(self):
        return not self.has_parent()

    def get_children(self):
        children = Category.objects.filter(parent=self)
        return children

    def is_leaf(self):
        children = self.get_children()
        if children:
            return False
        else:
            return True

    def is_middle(self):
        return not (self.is_top() or self.is_leaf())

    def get_url(self):
        return reverse('category', kwargs={'pk': self.pk})

class CategoryImage(models.Model):
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='category/other')

    def __str__(self):
        return self.category.name

class Script(models.Model):
    name = models.CharField(max_length=50)
    short_desc = models.TextField()
    full_desc = models.TextField(null=True, blank=True)
    start = models.ImageField(upload_to='script/start')
    end = models.ImageField(upload_to='script/end')
    load_file = models.FileField(upload_to='script/file')
    category = models.ForeignKey(Category)
    shutter_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def get_url(self):
        return reverse('script', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def get_full_desc(self):
        if self.full_desc:
            return self.full_desc
        else:
            return self.short_desc

    def comment_count(self):
        comments = Comment.objects.filter(object_pk=self.pk)
        return len(comments)

class ScriptParam(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField()
    script = models.ForeignKey(Script)
    default_value = models.TextField(null=True, blank=True)

    def __str__(self):
        result = '%s: %s, default_value: %s'%(self.script.name,self.name,self.default_value)
        return result

class ScriptModerator(CommentModerator):
    email_notification = True
moderator.register(Script, ScriptModerator)
