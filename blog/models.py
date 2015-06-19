from django.db import models

#entry category
class Category(models.Model):
    title = models.CharField(max_length=255)
    entry_num = models.IntegerField(default=0)
    modify_date = models.DateTimeField(auto_created=True, auto_now=True)

    def __unicode__(self):
        return u'%s' % self.title

from DjangoUeditor.models import UEditorField
#entry
class Entry(models.Model):
    category = models.ForeignKey("Category", verbose_name="entry category")
    title = models.CharField(max_length=255)
    content = UEditorField("content")
    hits = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_created=True, auto_now=True)
    modify_date = models.DateTimeField(auto_created=True, auto_now=True)

    def __unicode__(self):
        return u'%s' % self.title

class Comment(models.Model):
    name = models.CharField(max_length=128, default="exmaple")
    email = models.EmailField(default="example@gmail.com")
    entry = models.ForeignKey("Entry", verbose_name="comment entry")
    content = models.TextField()
    comment_date = models.DateTimeField(auto_created=True, auto_now=True)

    def __unicode__(self):
        return self.content