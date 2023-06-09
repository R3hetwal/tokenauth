from django.contrib import admin
from api.models import Project, Department, Document
from django.http import HttpResponse
import csv
import xlwt

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description', 'start_date', 'complete')
    list_filter = ('start_date', 'complete')
    actions = ['export_as_csv', 'export_as_xls']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="projects.csv"'
        writer = csv.writer(response)
        writer.writerow(['Project Name', 'Description', 'Start Date', 'Complete'])
        for project in queryset:
            writer.writerow([project.project_name, project.description, project.start_date, project.complete])
        return response
    export_as_csv.short_description = "Export selected as CSV"

    def export_as_xls(self, request, queryset):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="projects.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Projects')
        row_num = 0
        columns = ['Project Name', 'Description', 'Start Date', 'Complete']
        for col_num, column_title in enumerate(columns):
            ws.write(row_num, col_num, column_title)
        for project in queryset:
            row_num += 1
            row = [project.project_name, project.description, project.start_date, project.complete]
            for col_num, cell_value in enumerate(row):
                ws.write(row_num, col_num, cell_value)
        wb.save(response)
        return response
    export_as_xls.short_description = "Export selected as XLS"

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'content', 'created_at', 'identifier')
    list_filter = ('created_at',)
    search_fields = ('identifier',)
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="documents.csv"'
        writer = csv.writer(response)
        writer.writerow(['Document Name', 'Content', 'Identifier', 'Created At'])
        for document in queryset:
            writer.writerow([document.document_name, document.content, document.identifier, document.created_at])
        return response
    export_as_csv.short_description = "Export selected as CSV"

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'department_head', 'joined_date')
    list_filter = ('project', 'department_name')
    actions = ['export_as_csv'] 

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="departments.csv"'
        writer = csv.writer(response)
        writer.writerow(['Department Name', 'Department Head', 'Members', 'Joined Date', 'Projects'])
        for department in queryset:
            # Get the members as a comma-separated string
            members = ', '.join([str(member) for member in department.members.all()])
            # Get the projects as a comma-separated string
            projects = ', '.join([str(project) for project in department.project.all()])
            writer.writerow([department.department_name, department.department_head, members, department.joined_date, projects])
        return response
    export_as_csv.short_description = "Export selected as CSV"


admin.site.register(Project, ProjectAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Department, DepartmentAdmin)
