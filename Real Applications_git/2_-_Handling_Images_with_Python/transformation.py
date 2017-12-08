"""Autores: David Alejandro Ayala Palacios, Efren Santiago Landeros"""
"""Descripccion: se muestra la imagen transformada, es decir se imprime al volteada"""
from PIL import Image

img = Image.open("a.jpg")

spin = img.transpose(Image.ROTATE_270)

spin.show()