"""Descarga los datasets del Proyecto integrador de py401 a data/proyecto/.

Uso (desde la raíz del repositorio, en la terminal del Codespace):

    python tools/descargar_datasets.py --lista
    python tools/descargar_datasets.py diamonds
    python tools/descargar_datasets.py adult bike wine
    python tools/descargar_datasets.py todos --originales

Solo usa la biblioteca estándar y pandas (para verificar que cada archivo se lee).
Cada dataset se guarda como un CSV con encabezados en data/proyecto/<nombre>.csv.
Con --originales también se descarga el ZIP oficial del UCI ML Repository y se
extrae en data/proyecto/<nombre>_originales/ (incluye la documentación .names o
Readme.txt y, en Bike Sharing, el archivo diario day.csv).
"""
import argparse
import os
import sys
import time
import urllib.error
import urllib.request
import zipfile

import pandas as pd

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "data", "proyecto")

DATASETS = {
    "diamonds": {
        "titulo": "diamonds (Seaborn / ggplot2)",
        "csv": "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv",
        "zip": None,
        "filas": 53940,
    },
    "adult": {
        "titulo": "Adult / Census Income (UCI, id 2)",
        "csv": "https://archive.ics.uci.edu/static/public/2/data.csv",
        "zip": "https://archive.ics.uci.edu/static/public/2/adult.zip",
        "filas": 48842,
    },
    "bike": {
        "titulo": "Bike Sharing, datos por hora (UCI, id 275)",
        "csv": "https://archive.ics.uci.edu/static/public/275/data.csv",
        "zip": "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip",
        "filas": 17379,
    },
    "wine": {
        "titulo": "Wine Quality, tinto y blanco con columna color (UCI, id 186)",
        "csv": "https://archive.ics.uci.edu/static/public/186/data.csv",
        "zip": "https://archive.ics.uci.edu/static/public/186/wine+quality.zip",
        "filas": 6497,
    },
}


def bajar(url, ruta, intentos=3, espera=3, timeout=60):
    """Descarga `url` a `ruta` (vía un archivo temporal) y devuelve el tamaño en bytes."""
    temporal = ruta + ".parcial"
    for intento in range(1, intentos + 1):
        try:
            peticion = urllib.request.Request(url, headers={"User-Agent": "py401-descargar-datasets"})
            with urllib.request.urlopen(peticion, timeout=timeout) as respuesta, open(temporal, "wb") as archivo:
                while bloque := respuesta.read(1 << 16):
                    archivo.write(bloque)
            os.replace(temporal, ruta)
            return os.path.getsize(ruta)
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            if os.path.exists(temporal):
                os.remove(temporal)
            if intento == intentos:
                raise
            print(f"   intento {intento} falló ({error}); reintentando en {espera} s…")
            time.sleep(espera)


def descargar(nombre, destino=DESTINO, forzar=False, originales=False):
    """Descarga un dataset, verifica que pandas lo lea y devuelve la ruta del CSV."""
    if nombre not in DATASETS:
        raise ValueError(f"clave desconocida {nombre!r}; usa una de: {', '.join(DATASETS)}")
    info = DATASETS[nombre]
    os.makedirs(destino, exist_ok=True)
    ruta_csv = os.path.join(destino, f"{nombre}.csv")
    if os.path.isfile(ruta_csv) and not forzar:
        print(f"= {nombre}: ya existe {os.path.relpath(ruta_csv, RAIZ)} (usa --forzar para volver a bajarlo)")
    else:
        print(f"↓ {info['titulo']}\n   {info['csv']}")
        tamano = bajar(info["csv"], ruta_csv)
        print(f"   {tamano / 1024 / 1024:.2f} MiB")
    datos = pd.read_csv(ruta_csv)
    estado = "OK" if len(datos) == info["filas"] else f"AVISO: se esperaban {info['filas']} filas"
    print(f"   {datos.shape[0]} filas × {datos.shape[1]} columnas → {estado}")
    if originales and info["zip"]:
        ruta_zip = os.path.join(destino, f"{nombre}_originales.zip")
        print(f"↓ ZIP original\n   {info['zip']}")
        tamano = bajar(info["zip"], ruta_zip)
        carpeta = os.path.join(destino, f"{nombre}_originales")
        with zipfile.ZipFile(ruta_zip) as archivo_zip:
            archivo_zip.extractall(carpeta)
            print(f"   {tamano / 1024:.0f} KiB; extraído en {os.path.relpath(carpeta, RAIZ)}: {', '.join(archivo_zip.namelist())}")
        os.remove(ruta_zip)
    return ruta_csv


def main():
    parser = argparse.ArgumentParser(description="Descarga los datasets del Proyecto integrador a data/proyecto/.")
    parser.add_argument("datasets", nargs="*", help=f"uno o varios de: {', '.join(DATASETS)}, o 'todos'")
    parser.add_argument("--lista", action="store_true", help="muestra los datasets disponibles y sus URL")
    parser.add_argument("--forzar", action="store_true", help="vuelve a descargar aunque el archivo ya exista")
    parser.add_argument("--originales", action="store_true", help="descarga y extrae también el ZIP oficial del UCI")
    parser.add_argument("--destino", default=DESTINO, help="carpeta de destino (por defecto data/proyecto/)")
    argumentos = parser.parse_args()

    if argumentos.lista or not argumentos.datasets:
        for nombre, info in DATASETS.items():
            print(f"{nombre:9s} {info['titulo']}\n          CSV: {info['csv']}" + (f"\n          ZIP: {info['zip']}" if info["zip"] else ""))
        return 0
    elegidos = list(DATASETS) if "todos" in argumentos.datasets else argumentos.datasets
    desconocidos = [d for d in elegidos if d not in DATASETS]
    if desconocidos:
        parser.error(f"datasets desconocidos: {', '.join(desconocidos)}")

    fallas = []
    for nombre in elegidos:
        try:
            descargar(nombre, argumentos.destino, argumentos.forzar, argumentos.originales)
        except Exception as error:  # se informa y se sigue con los demás
            fallas.append(nombre)
            print(f"✗ {nombre}: no se pudo descargar ({error}). Revisa tu conexión o consulta data/DATASETS.md.")
    if fallas:
        print(f"\nFallaron: {', '.join(fallas)}")
        return 1
    print(f"\nListo. Archivos en {os.path.relpath(argumentos.destino, RAIZ) if argumentos.destino.startswith(RAIZ) else argumentos.destino}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
