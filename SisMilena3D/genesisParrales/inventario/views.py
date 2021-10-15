from django.shortcuts import render,HttpResponse
from .models import grupo,cliente,proveedor,producto
from django.views.generic.list import ListView
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from reportlab.pdfgen import canvas
# Create your views here.
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from django.contrib.auth.mixins import LoginRequiredMixin


class grupolistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = grupo
    template_name = 'mantenimientos/grupolistar.html'

class grupoguardar(CreateView):
    model = grupo
    fields = ['gruponombre','grupoanulado']
    template_name = 'mantenimientos/grupoguardar.html'
    success_url = reverse_lazy('grupolistar')

class grupomodificar(UpdateView):
    model = grupo
    fields = ['gruponombre','grupoanulado']
    template_name = 'mantenimientos/grupomodificar.html'
    success_url = reverse_lazy('grupolistar')

def hello_pdf(request):
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename=hello.pdf'

# Cree el objeto PDF, utilizando el objeto de respuesta como su "archivo".
  p = canvas.Canvas(response)

# Cree el objeto PDF, utilizando el objeto de respuesta como su "archivo".
# Consulte la documentación de ReportLab para obtener la lista completa de funciones.
  p.drawString(100, 100, "Hello world.")

# Cierre el objeto PDF limpiamente y listo.
  p.showPage()
  p.save()
  return response



def grupos_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   categorias = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Grupos", styles['Heading1'])
   categorias.append(header)
   headings = ('Id', 'Grupo', 'Activo')
   if not pk:
      todosgrupos = [(p.id, p.gruponombre, p.grupoanulado)
                         for p in grupo.objects.all().order_by('pk')]
   else:
      todosgrupos = [(p.id, p.gruponombre, p.grupoanulado)
                         for p in grupo.objects.filter(id=pk)]
   t = Table([headings] + todosgrupos)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))

   categorias.append(t)
   doc.build(categorias)
   response.write(buff.getvalue())
   buff.close()
   return response

###################################cliente###########################################
class clientelistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = cliente
    template_name = 'mantenimientos/clientelistar.html'

class clienteguardar(CreateView):
    model = cliente
    fields = ['clientecedula','clientenombre','clientetelefono', 'clienteanulado']
    template_name = 'mantenimientos/clienteguardar.html'
    success_url = reverse_lazy('clientelistar')

class clientemodificar(UpdateView):
    model = cliente
    fields = ['clientecedula', 'clientenombre', 'clientetelefono', 'clienteanulado']
    template_name = 'mantenimientos/clientemodificar.html'
    success_url = reverse_lazy('clientelistar')


def clientes_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   clientes = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Clientes", styles['Heading1'])
   clientes.append(header)
   headings = ('Id', 'Cedula','Nombre','Telefono', 'Activo')
   if not pk:
      todosclientes = [(p.id,p.clientecedula, p.clientenombre,p.clientetelefono, p.clienteanulado)
                         for p in cliente.objects.all().order_by('pk')]
   else:
      todosclientes = [(p.id,p.clientecedula, p.clientenombre,p.clientetelefono, p.clienteanulado)
                         for p in cliente.objects.filter(id=pk)]
   t = Table([headings] + todosclientes)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (5, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))

   clientes.append(t)
   doc.build(clientes)
   response.write(buff.getvalue())
   buff.close()
   return response

###################################proveedor###########################################

class proveedorlistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = proveedor
    template_name = 'mantenimientos/proveedorlistar.html'

class proveedorguardar(CreateView):
    model = proveedor
    fields = ['proveedorcedula','proveedornombre','proveedortelefono', 'proveedoranulado']
    template_name = 'mantenimientos/proveedorguardar.html'
    success_url = reverse_lazy('proveedorlistar')

class proveedormodificar(UpdateView):
    model = proveedor
    fields = ['proveedorcedula','proveedornombre','proveedortelefono', 'proveedoranulado']
    template_name = 'mantenimientos/proveedormodificar.html'
    success_url = reverse_lazy('proveedorlistar')


def proveedores_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   proveedores = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Proveedores", styles['Heading1'])
   proveedores.append(header)
   headings = ('Id', 'Cedula','Nombre','Telefono', 'Activo')
   if not pk:
      todosproveedores = [(p.id,p.proveedorcedula, p.proveedornombre ,p.proveedortelefono, p.proveedoranulado)
                         for p in proveedor.objects.all().order_by('pk')]
   else:
      todosproveedores = [(p.id,p.proveedorcedula, p.proveedornombre,p.proveedortelefono, p.proveedoranulado)
                         for p in proveedor.objects.filter(id=pk)]
   t = Table([headings] + todosproveedores)
   t.setStyle(TableStyle(
      [
         ('GRID', (0, 0), (5, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
      ]
   ))

   proveedores.append(t)
   doc.build(proveedores)
   response.write(buff.getvalue())
   buff.close()
   return response
#################################producto#########################

class productolistar(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = producto
    template_name = 'mantenimientos/productolistar.html'

class productoguardar(CreateView):
    model = producto
    fields = ['productogrupo','productonombre','productopreciovta','productocodigo','productoexistencia', 'productoanulado']
    template_name = 'mantenimientos/productoguardar.html'
    success_url = reverse_lazy('productolistar')

class productomodificar(UpdateView):
    model = producto
    fields = ['productogrupo','productonombre','productopreciovta','productocodigo','productoexistencia' ,'productoanulado']
    template_name = 'mantenimientos/productomodificar.html'
    success_url = reverse_lazy('productolistar')


def productos_print(self, pk=None):
   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
                           pagesize=letter,
                           rightMargin=40,
                           leftMargin=40,
                           topMargin=60,
                           bottomMargin=18,
                           )
   productos = []
   styles = getSampleStyleSheet()
   header = Paragraph("Listado de Productos", styles['Heading1'])
   productos.append(header)
   headings = ('Id', 'Grupo', 'Nombre', 'Preciovta', 'Codigo', 'Existencia', 'Activo')
   if not pk:
       todosproductos = [(p.id, p.productogrupo, p.productonombre, p.productopreciovta, p.productocodigo,
                         p.productoexistencia, p.productoanulado)
                           for p in producto.objects.all().order_by('pk')]
   else:
       todosproductos = [(p.id, p.productogrupo, p.productonombre, p.productopreciovta, p.productocodigo,
                         p.productoexistencia, p.productoanulado)
                           for p in producto.objects.filter(id=pk)]
   t = Table([headings] + todosproductos)
   t.setStyle(TableStyle(
       [
           ('GRID', (0, 0), (7, -1), 1, colors.dodgerblue),
           ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
           ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
       ]
   ))

   productos.append(t)
   doc.build(productos)
   response.write(buff.getvalue())
   buff.close()
   return response
