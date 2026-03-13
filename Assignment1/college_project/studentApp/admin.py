from django.contrib import admin
from .models import Student, Department
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','roll_number','department','created')
    list_filter = ('department','created')
    search_fields = ('name','roll_number')
    ordering = ('name',)


admin.site.register(Student, StudentAdmin)
admin.site.register(Department)