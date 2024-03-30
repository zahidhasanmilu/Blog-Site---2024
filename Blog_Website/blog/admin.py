from django.contrib import admin
from blog.models import Category, Tag, Blog, Comment, Reply

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_date')



# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Reply)