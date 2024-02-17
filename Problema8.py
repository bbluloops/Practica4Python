import sqlite3
import requests

def obtener_tipo_cambio_sunat():
    try:
        response = requests.get('https://api.apis.net.pe/v1/tipo-cambio-sunat')
        response.raise_for_status()
        data = response.json()
        print("Respuesta de la API de SUNAT:", data)
        return data
    except requests.RequestException as e:
        print("Error al obtener el tipo de cambio de SUNAT:", e)
        return None

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def crear_tabla_bitcoin():
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                            fecha TEXT PRIMARY KEY,
                            precio_usd REAL,
                            precio_gbp REAL,
                            precio_eur REAL,
                            precio_pen REAL
                          )''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error al crear la tabla 'bitcoin':", e)

def insertar_datos_bitcoin(fecha, precios):
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT OR IGNORE INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) 
                          VALUES (?, ?, ?, ?, ?)''', (fecha, precios['USD'], precios['GBP'], precios['EUR'], precios['PEN']))
        conn.commit()
        conn.close()
        print("Datos de Bitcoin insertados correctamente en la tabla 'bitcoin'.")
    except sqlite3.Error as e:
        print("Error al insertar los datos de Bitcoin:", e)

def calcular_precio_bitcoins(monto, moneda):
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1''')
        row = cursor.fetchone()
        if row:
            precio_pen, precio_eur = row
            if moneda.upper() == 'PEN':
                precio_total = monto * precio_pen
                print(f"El precio de compra de {monto} bitcoins en PEN es: {precio_total:.2f} PEN")
            elif moneda.upper() == 'EUR':
                precio_total = monto * precio_eur
                print(f"El precio de compra de {monto} bitcoins en EUR es: {precio_total:.2f} EUR")
            else:
                print("Moneda no válida. Por favor, ingrese 'PEN' o 'EUR'.")
        else:
            print("No se encontraron datos de Bitcoin en la base de datos.")
        conn.close()
    except sqlite3.Error as e:
        print("Error al calcular el precio de compra de bitcoins:", e)

def main():
    tipo_cambio = obtener_tipo_cambio_sunat()
    if tipo_cambio:
        precios_bitcoin = obtener_precio_bitcoin()
        if precios_bitcoin:
            fecha = precios_bitcoin['time']['updatedISO'][:10]
            precios = {
                'USD': precios_bitcoin['bpi']['USD']['rate_float'],
                'GBP': precios_bitcoin['bpi']['GBP']['rate_float'],
                'EUR': precios_bitcoin['bpi']['EUR']['rate_float'],
                'PEN': tipo_cambio['venta']
            }
            crear_tabla_bitcoin()
            insertar_datos_bitcoin(fecha, precios)
            calcular_precio_bitcoins(10, 'PEN')
            calcular_precio_bitcoins(10, 'EUR')

if __name__ == "__main__":
    main()

