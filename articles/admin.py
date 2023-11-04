from django.contrib import admin
from .models import Article ,Comment
# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment

admin.site.register(Article)
admin.site.register(Comment)