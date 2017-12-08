"""Muestra los robots.txt que estan permitidos o no en el dominio establecido"""
"""Autores: Efrén Santiago Landeros Hernández
            David Alejandro Ayala Palacios """
import urllib.request
import io


def get_robots_txt(url):

    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    req = urllib.request.urlopen(path + "robots.txt", data = None)
    data = io.TextIOWrapper(req, encoding = 'utf-8')

    return data.read()


print(get_robots_txt('https://www.reddit.com'))