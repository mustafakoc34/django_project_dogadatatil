from django.contrib import admin
from .models import *

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name","title")
    search_fields =("karavan_category__title",)

admin.site.register(Karavanlar)
admin.site.register(Bungalov)
admin.site.register(Tent)
admin.site.register(Comment, CommentAdmin)
