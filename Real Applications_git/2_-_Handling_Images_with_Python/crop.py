"""Autores: David Alejandro Ayala Palacios, Efren Santiago Landeros"""
"""Descripccion: se muestra solamente el area de una parte de la imagen con los valores correspondientes"""
from PIL import Image

img = Image.open("976.jpg")

area = (100, 100, 200, 200)
cropped_img = img.crop(area)

cropped_img.show()