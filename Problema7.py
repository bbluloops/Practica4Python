import sqlite3
import requests

def obtener_tipo_cambio_mensual(year, month):
    try:
        url = f'https://api.apis.net.pe/v1/tipo-cambio-sunat?year={year}&month={month}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Error al obtener el tipo de cambio:", e)
        return None

def crear_tabla_sunat_info():
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                            fecha TEXT PRIMARY KEY,
                            compra REAL,
                            venta REAL
                          )''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error al crear la tabla:", e)

def insertar_datos_sunat_info(year, month, data):
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        for item in data:
            fecha = item['fecha']
            compra = item['compra']
            venta = item['venta']
            cursor.execute('''INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)''', (fecha, compra, venta))
        conn.commit()
        conn.close()
        print(f"Datos del año {year} y mes {month} insertados correctamente en la tabla 'sunat_info'.")
    except sqlite3.Error as e:
        print("Error al insertar los datos:", e)

def mostrar_contenido_tabla():
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM sunat_info''')
        rows = cursor.fetchall()
        print("Contenido de la tabla 'sunat_info':")
        for row in rows:
            print(row)
        conn.close()
    except sqlite3.Error as e:
        print("Error al mostrar el contenido de la tabla:", e)

def main():
    year = 2023
    for month in range(1, 13):
        data = obtener_tipo_cambio_mensual(year, month)
        if data:
            crear_tabla_sunat_info()
            insertar_datos_sunat_info(year, month, data)
    mostrar_contenido_tabla()

if __name__ == "__main__":
    main()

