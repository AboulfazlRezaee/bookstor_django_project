from django.contrib import admin
from .models import Book, Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created', 'recommend', 'status')


admin.site.register(Book)
# admin.site.register(Comment, CommentAdmin)