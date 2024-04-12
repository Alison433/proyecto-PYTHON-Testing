from django.contrib import admin
from .models import City, Role, Contact, Client_Type, Position_Specialty, Time_Work, Availability_Status, CustomUser, Client, Position, Employee, Identification_type
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
    
    # pdf.setFont('Helvetica-Bold', 12)
    # pdf.drawString(480, 750, 'Hola care bola')

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

@admin.register(City)
class cityAdmin(ImportExportModelAdmin):
    list_display = ['city_name']
    search_fields = ['city_name']
    list_per_page = 10 
    actions = [download_pdf]

@admin.register(Role)
class roleAdmin(ImportExportModelAdmin):
    list_display = ['name_role', 'role_description']
    search_fields = ['name_role']
    list_filter = ['name_role']
    list_editable = ['role_description']
    list_per_page = 10 
    actions = [download_pdf]

@admin.register(Contact)
class contactAdmin(ImportExportModelAdmin):
    list_display = ['address', 'city']
    search_fields = ['address']
    list_filter = ['city']
    list_display_links = ['address']
    list_per_page = 10 
    actions = [download_pdf]
    
@admin.register(Identification_type)
class identification_typeAdmin(ImportExportModelAdmin):
    list_display = ['identification_type', 'description_type_identification']
    list_filter = ['identification_type']
    list_display_links = ['identification_type']
    list_per_page = 10 
    actions = [download_pdf]

@admin.register(Client_Type)
class client_typeAdmin(ImportExportModelAdmin):
    list_display = ['client_type_name', 'client_type_description']
    search_fields = ['client_type_name']
    list_filter = ['client_type_name']
    list_editable = ['client_type_description']
    list_per_page = 10 
    actions = [download_pdf]

if not admin.site.is_registered(Position_Specialty):
    @admin.register(Position_Specialty)
    class position_specialtyAdmin(ImportExportModelAdmin):
        list_display = ['name_specialty_position', 'description_specialty_position', 'position',]
        search_fields = ['name_specialty_position']
        list_filter = ['name_specialty_position', 'position']
        list_editable = ['description_specialty_position']
        list_per_page = 10 
        actions = [download_pdf]

@admin.register(Time_Work)
class time_workAdmin(ImportExportModelAdmin):
    list_display = ['work_time_type', 'work_time_description']
    search_fields = ['work_time_type']
    list_filter = ['work_time_type']
    list_editable = ['work_time_description']
    list_per_page = 10 
    actions = [download_pdf]

if not admin.site.is_registered(Availability_Status):
    @admin.register(Availability_Status)
    class availability_statusAdmin(ImportExportModelAdmin):
        list_display = ['availability_type', 'description_type_availability']
        search_fields = ['availability_type']
        list_filter = ['availability_type']
        list_editable = ['description_type_availability']
        list_per_page = 10 
        actions = [download_pdf]

@admin.register(CustomUser)
class customuser_Admin(ImportExportModelAdmin):
    list_display = ['username', 'email', 'phone', 'birth_date', 'role', 'identification_type', 'contact']
    search_fields = ['username', 'email']
    list_filter = ['role']
    list_editable = ['email', 'phone']
    list_per_page = 10 
    actions = [download_pdf]

@admin.register(Client)
class clientAdmin(ImportExportModelAdmin):
    list_display = ['user', 'client_type']
    search_fields = ['user__username']
    list_filter = ['client_type']
    list_editable = ['client_type']
    list_per_page = 10 
    actions = [download_pdf]

@admin.register(Position)
class positionAdmin(ImportExportModelAdmin):
    list_display = ['name_position']
    search_fields = ['name_position']
    list_filter = ['name_position']

    list_per_page = 10 
    actions = [download_pdf]

@admin.register(Employee)
class employeeAdmin(ImportExportModelAdmin):
    list_display = ['user', 'work_time', 'position', 'availability_status']
    search_fields = ['user__username']
    list_filter = ['work_time', 'position', 'availability_status']
    list_editable = ['work_time', 'position', 'availability_status']
    list_per_page = 10 
    actions = [download_pdf]

class CityResource(resources.ModelResource):
    class Meta:
        model = City
        fields = ('city_name')
        actions = [download_pdf]

class RoleResource(resources.ModelResource):
    class Meta:
        model = Role
        fields = ('name_role', 'role_description')
        actions = [download_pdf]

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        fields = ('address', 'city')
        actions = [download_pdf]
        
class Identification_TypeResource(resources.ModelResource):
    class Meta:
        model = Contact
        fields = ('identification_type', 'description_type_identification')
        actions = [download_pdf]

class Client_TypeResource(resources.ModelResource):
    class Meta:
        model = Client_Type
        fields = ('client_type_name', 'client_type_description')
        actions = [download_pdf]

class Position_SpecialtyResource(resources.ModelResource):
    class Meta:
        model = Position_Specialty
        fields = ('name_specialty_position', 'description_specialty_position', 'position')
        actions = [download_pdf]

class Time_WorkResource(resources.ModelResource):
    class Meta:
        model = Time_Work
        fields = ('work_time_type', 'work_time_description')
        actions = [download_pdf]

class Availability_StatusResource(resources.ModelResource):
    class Meta:
        model = Availability_Status
        fields = ('availability_type', 'description_type_availability')
        actions = [download_pdf]

class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'birth_date', 'role', 'identification_type', 'contact')
        actions = [download_pdf]

class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        fields = ('user', 'client_type')
        actions = [download_pdf]

class PositionResource(resources.ModelResource):
    class Meta:
        model = Position
        fields = ('name_position')
        actions = [download_pdf]

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        fields = ('user', 'work_time', 'position', 'availability_status')
        actions = [download_pdf]

