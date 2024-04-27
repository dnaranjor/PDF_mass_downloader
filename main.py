import os
import requests

def descargar_pdf(url, nombre_archivo):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    chunk_size = 1024
    bytes_so_far = 0
    
    with open(nombre_archivo, 'wb') as f:
        for chunk in response.iter_content(chunk_size):
            if chunk:
                f.write(chunk)
                bytes_so_far += len(chunk)
                porcentaje = (bytes_so_far / total_size) * 100
                print(f"Descargando {nombre_archivo}: {porcentaje:.2f}% completado", end='\r')
    print()

def main():
    # Crear la carpeta "downloads" si no existe
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    # Leer el archivo de texto
    with open("enlaces.txt", "r") as file:
        for idx, line in enumerate(file, start=1):
            url = line.strip()
            nombre_archivo = f"downloads/archivo_{idx}.pdf"
            descargar_pdf(url, nombre_archivo)

if __name__ == "__main__":
    main()

