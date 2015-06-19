from django.contrib import admin
from blog.models import Entry, Comment, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'entry_num')
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'hits', 'modify_date', 'post_date')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('entry', 'content', 'comment_date', 'name', 'email')
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment, CommentAdmin)
