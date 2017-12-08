"""Este codigo te permite descargar imagenes de internet"""
"""Autores: Efrén Santiago Landeros Hernández
            David Alejandro Ayala Palacios """
import random
import urllib.request

def download_web_image(url):

    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOCJRQWSI_V2zQxNjhRyDfvHL3Z5iU90sHe5NRCJenYCP-wGZw")
