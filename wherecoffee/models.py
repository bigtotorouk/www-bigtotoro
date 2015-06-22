#coding:utf-8
from django.db import models

# Create your models here.
class Coffee(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"名称")
    category = models.CharField(max_length=50, blank=True, verbose_name=u"种类")
    desc = models.CharField(max_length=200, blank=True, verbose_name=u"详情介绍")
    price_old = models.FloatField(blank=True,default=0.0, verbose_name=u"原价")
    price_new = models.FloatField(blank=True,default=0.0, verbose_name=u"现价")
    img0 = models.ImageField(upload_to='wherecoffee/coffee/', blank=True, verbose_name=u"图片1")
    img1 = models.ImageField(upload_to='wherecoffee/coffee/', blank=True, verbose_name=u"图片2")
    img2 = models.ImageField(upload_to='wherecoffee/coffee/', blank=True, verbose_name=u"图片3")

    class Meta:
        verbose_name = u"产品 - Coffee"
    def __unicode__(self):
    # 在Python3中使用 def __str__(self)
        return self.title

class Order(models.Model):

    nicker = models.CharField(max_length=50, verbose_name=u"称呼")
    coffee = models.ForeignKey(Coffee,null=True, blank=True, verbose_name=u"咖啡")
    location = models.CharField(max_length=100,verbose_name=u"地址")
    tel = models.CharField(max_length=50,verbose_name=u"电话(联系方式)")
    licence = models.CharField(max_length=100, blank=True, verbose_name=u"序列号")
    state = models.CharField(max_length=100, blank=True, verbose_name=u"状态", choices=(['0', u'新建'],[ '1', u'进行中'],[ '2', u'完成']))

    create_time = models.DateTimeField(auto_now_add=True,verbose_name=u"创建时间")
    modify_time = models.DateTimeField(auto_now_add=True,verbose_name=u"修改时间")

    class Meta:
        verbose_name = u"订单 - Coffee"

    def __unicode__(self):
        return self.nicker