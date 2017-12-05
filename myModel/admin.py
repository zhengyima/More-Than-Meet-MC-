from django.contrib import admin
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

#import os
from myModel import models
class SellerAdmin(admin.ModelAdmin):
        list_display = ('sno','sname','sgender','sage','sheight','sxz','sschool','smajor','sgrade','stime','srange','swage','sinfo','simg','slike','scharm','snum')

class UserAdmin(admin.ModelAdmin):
	list_display = ('unickname','ugender','ucity','uprovince','ucountry','usigntime')

class OrderAdmin(admin.ModelAdmin):
        list_display = ('ono','sno','bno','bhour','bneed','bnote','otime','ostatus')

class SIAdmin(admin.ModelAdmin):
        list_display = ('ino','iurl','sno')

class SLAdmin(admin.ModelAdmin):
        list_display = ('lno','lname','sno')

class SDAdmin(admin.ModelAdmin):
        list_display = ('sno','sflag')
class SLikeAdmin(admin.ModelAdmin):
 	list_display = ('bno','sno')
'''
class ImgUploadAdmin(admin.ModelAdmin):
	username = models.CharField(max_length=30)
        headImg = models.FileField(upload_to='./images/')     
        def __unicode__(self):
                return self.username
'''
'''
class Article(models.Model):
	title = models.CharField('title', max_length=256)
    	content = models.TextField('content')
    	ph = models.ImageField('image',upload_to='uploadImages')

    	pub_date = models.DateTimeField('time', auto_now_add=True, editable = True)
    	#update_time = models.DateTimeField('update_time',auto_now=True, null=True)
'''
#admin.site.register(Article)
#admin.site.register(models.Orders)
admin.site.register(models.Seller,SellerAdmin)
admin.site.register(models.Users,UserAdmin)
admin.site.register(models.Orders,OrderAdmin)
admin.site.register(models.SellerImage,SIAdmin)
admin.site.register(models.SellerDisplay,SDAdmin)
admin.site.register(models.SellerLabel,SLAdmin)
admin.site.register(models.SellerLike,SLikeAdmin)
#admin.site.register(Article)
# Register your models here.
