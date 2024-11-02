import pdfkit
import jinja2

from datetime import datetime

name=input("Ingrese su nombre: ")
item1=input("Ingrese sus Nombres: ")
item2=input("Ingrese sus Apellidos: ")
item3=input("Ingrese su direccion: ")
item4=input("Ingrese su telefono: ")
date=datetime.today().strftime("%d %b, %Y")

contenido = {
    'name': name,
    'item1': item1,
    'item2': item2,
    'item3': item3,
    'item4': item4,
    'date': date
}

template_loader= jinja2.FileSystemLoader('./read_pdf')

template_env = jinja2.Environment(loader=template_loader)

file='schema.html'

#template y el_contrato son variables globales
template=template_env.get_template(file)
el_contrato=template.render(contenido)

config=pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

output_name='./read_pdf/contrato.pdf'
output=pdfkit.from_string(el_contrato, output_name, configuration=config)

print("Contrato generado con éxito")