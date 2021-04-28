from service.genera_seccion_sumas_aritmeticas import GeneraSumas as gs
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Enumerate
from pylatex.utils import italic

ejercicios_suma = gs(cantidad_sumas= 10, sumandos= 10, limite_superior= 100, limite_inferior=-100)
geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
doc = Document(geometry_options=geometry_options)
with doc.create(Section('Aritmética ')):
    doc.append('Esta es la sección destinada a aritmética.')
    with doc.create(Subsection('Sumas')):
        doc.append('Resuelva correctamente las siguientes sumas:')
        with doc.create(Enumerate()) as enum:
            for ejercicio in ejercicios_suma.ejercicios:
                enum.add_item(ejercicio.__str__())

doc.generate_pdf('/tmp/ejercicios', clean_tex=True)
