"""Autores: David Alejandro Ayala Palacios, Efren Santiago Landeros"""
"""Descripccion: se muestra la imagen mas amplia aumenta su tamaño y formato"""
from PIL import Image
img = Image.open("976.jpg")

print(img.size)
print(img.format)

img.show()