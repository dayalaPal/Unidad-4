"""Autores: David Alejandro Ayala Palacios, Efren Santiago Landeros"""
"""Descripccion: se muestra la imagen 'a' con el area que le corresponde en los valores, insertandose en la imagen 976"""
from PIL import Image

img = Image.open("a.jpg")
img1 = Image.open("976.jpg")

area = (500,500,800,720)

img.paste(img1)

img.show()