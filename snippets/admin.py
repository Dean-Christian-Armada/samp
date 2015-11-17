from django.contrib import admin

from . models import *
# Register your models here.

admin.site.register(Students)
admin.site.register(Section)
admin.site.register(FavoriteNumber)
admin.site.register(FavoriteSubject)
admin.site.register(NamePicture)
admin.site.register(PictureFolders)
# admin.site.register(CommonInfo)
# admin.site.register(Student)