from django.db import models

#entry Message
class Message(models.Model):
    name = models.CharField(max_length=255,blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255,)
    pub_date = models.DateTimeField(auto_created=True, auto_now=True)

    def __unicode__(self):
        return u'%s' % self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=500,blank=True)
    img0 = models.ImageField(upload_to='company/%Y%m', blank=True)
    img1 = models.ImageField(upload_to='company/%Y%m', blank=True)
    img2 = models.ImageField(upload_to='company/%Y%m', blank=True)
    img3 = models.ImageField(upload_to='company/%Y%m', blank=True)
    img4 = models.ImageField(upload_to='company/%Y%m', blank=True)

    def __unicode__(self):
        return self.title