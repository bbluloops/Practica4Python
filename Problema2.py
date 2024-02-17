import random
from pyfiglet import Figlet

def obtener_fuente_usuario():
    f = Figlet()
    fuentes_disponibles = f.getFonts()
    fuente_seleccionada = input(f"Fuentes disponibles: {', '.join(fuentes_disponibles)}\nIngrese el nombre de la fuente que desea utilizar (o presione Enter para seleccionar una al azar): ").strip()
    if fuente_seleccionada == "":
        fuente_seleccionada = random.choice(fuentes_disponibles)
    return fuente_seleccionada

def main():
    fuente = obtener_fuente_usuario()
    texto = input("Ingrese el texto que desea imprimir: ")
    f = Figlet(font=fuente)
    texto_formateado = f.renderText(texto)
    print(texto_formateado)

if __name__ == "__main__":
    main()
