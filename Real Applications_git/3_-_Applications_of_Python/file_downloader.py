"""Este codigo permite descargar archivos .csv de internet"""
"""Autores: Efrén Santiago Landeros Hernández
            David Alejandro Ayala Palacios """
import urllib.request

google_stocks = "https://www.ibm.com/support/knowledgecenter/es/SVU13_7.2.1/com.ibm.ismsaas.doc/reference/AssetsImportCompleteSample.csv?view=kc"

def download_stock_data(url):

    response = urllib.request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'google.csv'
    fx = open(dest_url, "w")

    for line in lines:
        fx.write(line + "\n")

    fx.close()

download_stock_data(google_stocks)
