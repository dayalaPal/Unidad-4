"""Muestra que puertos activos que tiene el dominio"""
"""Autores: Efrén Santiago Landeros Hernández
            David Alejandro Ayala Palacios """
import os


def get_nmap(options, ip):

    command = "nmap " + options + " " + ip
    process = os.popen(command)

    results = str(process.read())

    return results


print(get_nmap('-F', '54.186.250.79'))

