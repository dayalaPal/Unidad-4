"""Autores: David Alejandro Ayala Palacios, Efren Santiago Landeros"""
"""Descripccion: se hace la union de imagen mas grande"""
from PIL import Image

img = Image.open("a.jpg")
r, g, b = img.split()

img_1 = Image.open("b.jpg")

r1, g1, b1 = img_1.split()

new_img = Image.merge("RGB", (r1,g1,b1))
new_img.show()

