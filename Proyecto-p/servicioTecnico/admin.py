from django.contrib import admin
from .models import Service_Status, Service_Type, Service, Scheduling
from registroUsuario.models import Availability_Status
from registroUsuario.models import Position_Specialty
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table,TableStyle
from reportlab.lib import colors
from django.http import HttpResponse

def download_pdf(self,request,queryset):
    model_name = self.model.__name__
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment;filename={model_name}.pdf'

    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle('PDF Reporte')

    ordered_queryset = queryset.order_by('id')
    headers = [field.verbose_name for field in self.model._meta.fields]
    data = [headers]
    for obj in queryset:
        data_row = [str(getattr(obj, field.name)) for field in self.model._meta.fields]
        data.append(data_row)
    
    table = Table(data)
    table.setStyle(TableStyle(
        [
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
        ]
    ))

    canvas_width = 600
    canvas_height = 600
    
    table.wrapOn(pdf, canvas_width, canvas_height)
    table.drawOn(pdf, 40, canvas_height - len(data))

    pdf.save()
    return response

download_pdf.short_description = 'Descargue aqui los items en formato pdf.'

@admin.register(Service_Status)
class ServiceStatusAdmin(ImportExportModelAdmin):
    list_display = ('service_status_name', 'service_status_description',)
    list_editable = ('service_status_description',)
    search_fields = ('service_status_name',)
    actions = [download_pdf]

@admin.register(Service_Type)
class ServiceTypeAdmin(ImportExportModelAdmin):
    list_display = ('service_type_name', 'service_type_description',)
    list_editable = ('service_type_description',)
    search_fields = ('service_type_name',)
    actions = [download_pdf]

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ('service_description', 'service_price', 'service_type', 'service_status', 'client')
    list_editable = ('service_price', 'service_status', )
    list_filter = ('client','service_type',)
    actions = [download_pdf]
    
@admin.register(Availability_Status)
class availability_statusAdmin(ImportExportModelAdmin):
    list_display = ('id', 'availability_type', 'description_type_availability')
    actions = [download_pdf]
    
@admin.register(Position_Specialty)
class position_specialtyAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name_specialty_position', 'description_specialty_position', 'position')
    list_editable = ('description_specialty_position',)  # Si quieres que sea editable desde la lista
    search_fields = ('name_specialty_position', )
    actions = [download_pdf]

@admin.register(Scheduling)
class SchedulingAdmin(ImportExportModelAdmin):
    list_display = ('scheduling_description', 'scheduling_time', 'scheduling_date', 'availability_status', 'service', 'employee',)
    list_filter = ('availability_status','service','employee',)
    list_editable = ('employee',)
    list_per_page = 10
    actions = [download_pdf]

class Service_StatusResource(resources.ModelResource):
    class Meta:
        model = Service_Status
        fields = ('service_status_name', 'service_status_description')
        actions = [download_pdf]

class Service_TypeResource(resources.ModelResource):
    class Meta:
        model = Service_Type
        fields = ('service_type_name', 'service_type_description')
        actions = [download_pdf]

class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service
        fields = ('service_description', 'service_price', 'service_type', 'service_status', 'client')
        actions = [download_pdf]

class SchedulingResource(resources.ModelResource):
    class Meta:
        model = Scheduling
        fields = ('scheduling_description', 'scheduling_time', 'scheduling_date', 'availability_status', 'service', 'employee')
        actions = [download_pdf]
        
class Availability_StatusResource(resources.ModelResource):
    class Meta:
        model = Availability_Status
        fields = ('id', 'availability_type', 'description_type_availability',)
        actions = [download_pdf]

class Position_SpecialtyResource(resources.ModelResource):
    class Meta:
        model = Position_Specialty
        fields = ('id', 'name_specialty_position', 'description_specialty_position', 'position')
        actions = [download_pdf]
