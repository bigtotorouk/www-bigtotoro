#coding:utf-8
from django.db import models
from bigtotoro.settings import AUTH_USER_MODEL
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class PeachUser(AbstractUser):
    photo = models.ImageField(upload_to='photos')
#
class Location(models.Model):
    parent_id = models.IntegerField()
    name = models.CharField(max_length=30)
    type = models.IntegerField()

    def __unicode__(self):
    # 在Python3中使用 def __str__(self)
        return self.name

#
# class ImageRes(models.Model):
#     im

class Peach(models.Model):

    title = models.CharField(max_length=100,verbose_name=u"标题")
    desc = models.CharField(max_length=200,verbose_name=u"描述")
    #location = models.OneToOneField(Location,verbose_name=u"位置",null=True, blank=True)
    img = models.ImageField(upload_to="peach/imgs",verbose_name=u"图片")

    province = models.CharField(verbose_name='省', max_length=50, blank=True,choices=())
    city= models.CharField(verbose_name='市', max_length=50, blank=True,choices=())
    area= models.CharField(verbose_name='区', max_length=50, blank=True,choices=())

    favors = models.ManyToManyField(PeachUser, related_name="favors", blank=True,verbose_name=u"收藏该对象的用户")
    likes = models.ManyToManyField(PeachUser, related_name="likes", blank=True,verbose_name=u"喜欢该对象的用户")

    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u"创建时间")
    modify_time = models.DateTimeField(auto_now_add=True,verbose_name=u"修改时间")

    class Meta:
        verbose_name = u"文章 - Peach"

    def __unicode__(self):
        return self.title





