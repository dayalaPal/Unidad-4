"""Autores: David Alejandro Ayala Palacios, Efren Santiago Landeros"""
"""Descripccion: se muestra la imagen en dos diferentes modos"""
from PIL import Image
from PIL import ImageFilter

img = Image.open("a.jpg")

img.show()
edges = img.filter(ImageFilter.FIND_EDGES)
edges.show()