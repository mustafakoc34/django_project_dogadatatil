from django.contrib import admin
from .models import *

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name","title","karavan_category")
    search_fields =("karavan_category__karavanModeli",)

admin.site.register(Karavanlar)
admin.site.register(Bungalov)
admin.site.register(Tent)
admin.site.register(Comment, CommentAdmin)
