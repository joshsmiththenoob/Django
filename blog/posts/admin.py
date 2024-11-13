from django.contrib import admin
from .models import Post
# Register your models here.
# Create the Model(Table) Admin Class 

"""
To see the Model(Table) and set display list of Model in Admin Page, Need to regirster
1. Model
2. the MdoelAdmin class which set the display list or links of Model in first argument
"""
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "post_title", "published_date"]
    list_display_links = ["id", "post_title"]
    list_filter = ["published_date"]
    search_fields = ["post_title"]
