import requests
import json

def get_ip_info(ip):
    url = "http://ip-api.com/json/" + ip
    response = requests.get(url)
    return response.json()

def main():
    results = []

    while True:
        ip = input("Ingresa una IP pública (o 'exit' para salir): ").strip()
        if ip.lower() == 'exit':
            break

        info = get_ip_info(ip)

        if info['status'] == 'success':
            result = {
                'IP': ip,
                'País': info.get('country'),
                'Región': info.get('regionName'),
                'ISP': info.get('isp'),
                'Coordenadas': {
                    'Latitud': info.get('lat'),
                    'Longitud': info.get('lon')
                }
            }

            print("País: " + str(result['País']))
            print("Región: " + str(result['Región']))
            print("ISP: " + str(result['ISP']))
            print("Coordenadas: " + str(result['Coordenadas']))
            
            results.append(result)
        else:
            print("No se pudo obtener la información de esta IP.")

    with open('resultados.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("Resultados guardados en resultados.json")

if __name__ == "__main__":
    main()
