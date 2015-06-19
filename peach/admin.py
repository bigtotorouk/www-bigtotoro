#coding:utf-8
from django.contrib import admin
from peach.models import PeachUser, Peach
from django import forms
from django.core.exceptions import ValidationError
# Register your models here.
#admin.site.register(PeachUser)

#https://github.com/django/django/blob/master/django/contrib/auth/models.py
class PeachUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'date_joined', 'photo')
    search_fields = ('username',)
    date_hierarchy = 'date_joined'
    fields = ('username', 'password', 'email', 'date_joined', 'photo')


from django.forms.fields import ChoiceField
from django.forms.fields import ValidationError
class MyChoiceField(ChoiceField):
    def validate(self, value):
        pass

class PeachForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PeachForm, self).__init__(*args, **kwargs)
        peach =  kwargs.get('instance', None)
        provinceChoices = ()
        cityChoices = ()
        areaChoices = ()
        if peach:
            provinceChoices = ([peach.province,peach.province],);
            cityChoices = ([peach.city,peach.city],);
            areaChoices = ([peach.area,peach.area],);
        self.fields['province'] = MyChoiceField(required=False, choices=provinceChoices)
        self.fields['city'] = MyChoiceField(required=False, choices=cityChoices)
        self.fields['area'] = MyChoiceField( required=False, choices=areaChoices)

    class Meta:
        model = Peach
        fields = '__all__' # Or a list of the fields that you want to include in your form

class PeachAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc',)
    search_fields = ('title',)
    date_hierarchy = 'create_time'
    # fieldsets = [
    #     (None,{'fields':['title','desc','img','favors','likes']}),
    #     ('位置',{'fields':['province','city','area']}),
    #     ('Date information',{'fields':['create_time'],'classes':['collapse']})
    #             ]
    form = PeachForm


admin.site.register(PeachUser, PeachUserAdmin)
admin.site.register(Peach, PeachAdmin)