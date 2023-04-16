from django.contrib import admin
from api.models import Project, Department, Document

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description', 'start_date', 'complete')
    list_filter = ('start_date', 'complete')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'created_at', 'identifier')
    list_filter = ('created_at',)
    search_fields = ('identifier',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_head')
    list_filter = ('project',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Department, DepartmentAdmin)