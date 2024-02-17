def contar_lineas_codigo(ruta_archivo):
    try:
        if not ruta_archivo.endswith(".py"):
            print("El archivo no es un archivo Python (.py)")
            return

        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            contador = 0
            for linea in lineas:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    contador += 1
            print(f"Archivo: '{ruta_archivo}', número de líneas de código: {contador}")
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print("Error:", e)

def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ").strip()
    contar_lineas_codigo(ruta_archivo)

if __name__ == "__main__":
    main()
