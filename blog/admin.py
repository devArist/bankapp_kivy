from django.contrib import admin
from blog import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'imageblog')
    search_fields = ('title',)


    def imageblog(self, obj):

        return mark_safe(f"<img src={obj.image.url} style='width:150px; height:90px' ")