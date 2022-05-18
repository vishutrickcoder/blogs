from django.contrib import admin
from .models import Category,Post

# Register your models here.

#for configracation of Category Admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','cat_id' ,'description', 'url', 'add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_id','url')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('js/script.js',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

