"""Muestra informacion del dominio"""
"""Autores: Efrén Santiago Landeros Hernández
            David Alejandro Ayala Palacios """
import os


def get_whois(url):

    command = "whois " + url
    process = os.popen(command)

    results = str(process.read())
    return results


print(get_whois('facebook.com'))