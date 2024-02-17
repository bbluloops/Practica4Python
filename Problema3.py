import requests
import zipfile
import os

# Descargar la imagen desde la URL
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_archivo_imagen = "imagen_descargada.jpg"

response = requests.get(url)
with open(nombre_archivo_imagen, 'wb') as f:
    f.write(response.content)

nombre_zip = "imagenes.zip"
with zipfile.ZipFile(nombre_zip, 'w') as zipf:
    zipf.write(nombre_archivo_imagen)

nombre_zip_comprimido = "imagenes_comprimidas.zip"
with zipfile.ZipFile(nombre_zip_comprimido, 'w') as zipf:
    zipf.write(nombre_zip)

os.remove(nombre_archivo_imagen)
os.remove(nombre_zip)

print("La imagen se ha descargado y comprimido correctamente en un archivo zip, que también ha sido comprimido en otro archivo zip.")
