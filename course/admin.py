from django.contrib import admin
from .models import Category,Course, Lesson, Comment, Quiz
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



class LessonCommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['lesson']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title','course','status','lesson_type']
    list_filter = ['status','lesson_type']
    search_fields = ['title', 'short_description','long_description']
    inlines = [LessonCommentInline]


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Category, SomeModelAdmin)
admin.site.register(Course, SomeModelAdmin)
admin.site.register(Lesson, SomeModelAdmin)
admin.site.register(Comment, SomeModelAdmin)
admin.site.register(Quiz, SomeModelAdmin)