from django.contrib import admin
from .models import Flow_Type, Inventory_Flow
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

@admin.register(Flow_Type)
class flow_typeAdmin(ImportExportModelAdmin):
    list_display = ('flow_type_name','flow_type_description',)
    search_fields = ('flow_type_name',)
    list_per_page = 10 
    actions = [download_pdf]

@admin.register(Inventory_Flow)
class inventory_flowAdmin(ImportExportModelAdmin):
    list_display = ('flow_type', 'product',)
    list_display_links = ('flow_type',)
    list_filter = ('product', 'flow_type')  # Agregamos 'product' como filtro
    list_per_page = 10 
    actions = [download_pdf]



class Flow_TypeResource(resources.ModelResource):
    class Meta:
        model = Flow_Type
        fields = ('flow_type_name','flow_type_description')
        actions = [download_pdf]

class Inventory_FlowResource(resources.ModelResource):
    class Meta:
        model = Inventory_Flow
        fields = ('flow_type', 'product')
        actions = [download_pdf]

