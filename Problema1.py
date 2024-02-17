import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        precio_en_usd = data['bpi']['USD']['rate_float']
        return precio_en_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def calcular_costo_bitcoins(bitcoins):
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_total = bitcoins * precio_bitcoin
        return costo_total
    else:
        return None

def main():
    try:
        bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
        costo_total = calcular_costo_bitcoins(bitcoins)
        if costo_total is not None:
            print(f"El costo actual de {bitcoins} bitcoins es: ${costo_total:,.4f}")
        else:
            print("No se pudo calcular el costo de los bitcoins.")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la cantidad de bitcoins.")

if __name__ == "__main__":
    main()
