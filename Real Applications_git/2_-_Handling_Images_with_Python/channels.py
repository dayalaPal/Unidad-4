"""Autores: David Alejandro Ayala Palacios, Efren Santiago Landeros"""
"""Descripccion: se muestra la imagen en tres presentaciones cada una con diferente estilo"""
from PIL import Image

img = Image.open("a.jpg")
r, g, b = img.split()

r.show()
g.show()
b.show()