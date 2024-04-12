from django.contrib import admin
from registroUsuario.models import CustomUser, Employee
from . models import Status_News_Order, Supplier_Order_Status, Suppliers, Supplier_Order, Supplier_Order_News
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

@admin.register(Status_News_Order)
class status_news_orderAdmin(ImportExportModelAdmin):
    list_display = ('status_news_order_name','status_news_order_description',)
    list_editable=('status_news_order_description',)
    search_fields = ('status_news_order_name',)
    list_per_page = 10
    actions = [download_pdf]

@admin.register(Supplier_Order_Status)
class supplier_order_statusAdmin(ImportExportModelAdmin):
    list_display = ('supplier_order_status_name', 'supplier_order_status_description',)
    list_filter = ('supplier_order_status_name', 'supplier_order_status_description',)
    list_editable = ('supplier_order_status_description',)
    list_per_page = 10
    actions = [download_pdf]

@admin.register(Suppliers)
class suppliersAdmin(ImportExportModelAdmin):
    list_display = ('supplier_name', 'supplier_address','supplier_email', 'supplier_nit', 'supplier_cellphone',)
    list_filter = ('supplier_name',)
    list_editable = ('supplier_address','supplier_email', 'supplier_nit', 'supplier_cellphone',)
    list_per_page = 10
    actions = [download_pdf]
    
@admin.register(Supplier_Order)
class supplier_orderAdmin(ImportExportModelAdmin):
    list_display = (
        'date_order', 'product_quantity', 'deliver_date', 'address', 'supplier_order_status', 'suppliers','order_price', 'employee','product',)
    list_editable = ('order_price', 'product_quantity', 'supplier_order_status','address',)
    list_filter = ('suppliers','employee',)
    list_display_links = ('suppliers',)
    list_per_page = 10
    actions = [download_pdf]

@admin.register(Supplier_Order_News)
class supplier_order_newsAdmin(ImportExportModelAdmin):
    list_display = ('date_new_order_supplier', 'status_news_order', 'supplier_order', 'employee',)
    list_filter = ('status_news_order','employee',)
    list_display_links = ('supplier_order',)
    list_per_page = 10
    actions = [download_pdf]

class Status_News_OrderResource(resources.ModelResource):
    class Meta:
        model = Status_News_Order
        fields = ('status_news_order_name','status_news_order_description')
        actions = [download_pdf]

class Supplier_Order_StatusResource(resources.ModelResource):
    class Meta:
        model = Supplier_Order_Status
        fields = ('supplier_order_status_name', 'supplier_order_status_description')
        actions = [download_pdf]

class SuppliersResource(resources.ModelResource):
    class Meta:
        model = Suppliers
        fields = ('supplier_name', 'supplier_address','supplier_email', 'supplier_nit', 'supplier_cellphone')
        actions = [download_pdf]

class Supplier_OrderResource(resources.ModelResource):
    class Meta:
        model = Supplier_Order
        fields = ('date_order', 'product_quantity', 'deliver_date', 'address', 'supplier_order_status', 'suppliers','order_price', 'employee','product')
        actions = [download_pdf]

class Supplier_Order_NewsResource(resources.ModelResource):
    class Meta:
        model = Supplier_Order_News
        fields = ('date_new_order_supplier', 'status_news_order', 'supplier_order', 'employee')
        actions = [download_pdf]