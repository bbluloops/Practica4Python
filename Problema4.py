import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP inapropiados
        data = response.json()
        precio_en_usd = data['bpi']['USD']['rate_float']
        return precio_en_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def guardar_precio_en_archivo(precio, nombre_archivo="precios_bitcoin.txt"):
    try:
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f"Precio: {precio:.4f} USD\n")
        print("Precio de Bitcoin guardado correctamente en el archivo.")
    except Exception as e:
        print("Error al guardar el precio de Bitcoin en el archivo:", e)

def main():
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        guardar_precio_en_archivo(precio_bitcoin)
    else:
        print("No se pudo obtener el precio de Bitcoin.")

if __name__ == "__main__":
    main()
