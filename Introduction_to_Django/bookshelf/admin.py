from django.contrib import admin
from .models import Book

# تخصيص عرض الموديل في Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # الأعمدة الظاهرة في القائمة
    search_fields = ('title', 'author')                     # إضافة البحث حسب العنوان أو المؤلف
    list_filter = ('publication_year',)                    # فلترة حسب سنة النشر

# تسجيل الموديل مع التخصيص
admin.site.register(Book, BookAdmin)
