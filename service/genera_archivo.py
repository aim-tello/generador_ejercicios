from service.genera_seccion_sumas_aritmeticas import GeneraSumas as gs
from service.genera_seccion_restas_aritmeticas import GeneraRestas as gr
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Enumerate
from pylatex.utils import italic

ejercicios_suma = gs(cantidad_sumas=10, sumandos=10, limite_superior=100, limite_inferior=-100)
ejercicios_resta = gr(cantidad_restas=10, sumandos=10, limite_superior=100, limite_inferior=-100)
geometry_options = {"tmargin": "1cm", "lmargin": "1cm"}
doc = Document(geometry_options=geometry_options)
with doc.create(Section('Aritmética ')):
    doc.append('Esta es la sección destinada a aritmética.')
    with doc.create(Subsection('Sumas')):
        doc.append('Resuelva correctamente las siguientes sumas:')
        with doc.create(Enumerate()) as enum:
            for ejercicio in ejercicios_suma.ejercicios:
                enum.add_item(ejercicio.__str__())
    with doc.create(Subsection('Restas')):
        doc.append('Resuelva correctamente las siguientes sumas:')
        with doc.create(Enumerate()) as enum:
            for ejercicio in ejercicios_resta.ejercicios:
                enum.add_item(ejercicio.__str__())

doc.generate_pdf('/tmp/ejercicios', clean_tex=True)
