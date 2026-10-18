# Datasets del Proyecto integrador (py401)

Los *datasets* del Proyecto integrador **no vienen en el repositorio**. Cada quien descarga el suyo a `data/proyecto/`, una carpeta que está en `.gitignore`, así que no se sube a GitHub (basta con documentar la fuente en el informe). Los datos de las sesiones (`penguins`, `titanic`, `tips`, `mpg`) sí vienen en `data/` y no requieren internet.

Las URL de esta página se probaron el 18 de octubre de 2026 (hora de la Ciudad de México). Los tamaños y las dimensiones son los de esa fecha.

| Clave | *Dataset* | Filas × columnas | CSV | ZIP original | Licencia |
|---|---|---|---|---|---|
| `diamonds` | Precios de diamantes | 53,940 × 10 | 2,772,143 bytes (2.6 MiB) | — | ver abajo |
| `adult` | Adult / Census Income | 48,842 × 15 | 5,347,052 bytes (5.1 MiB) | 620,237 bytes | CC BY 4.0 |
| `bike` | Bike Sharing (por hora) | 17,379 × 17 | 1,156,736 bytes (1.1 MiB) | 279,992 bytes | CC BY 4.0 |
| `wine` | Wine Quality (tinto + blanco) | 6,497 × 13 | 390,515 bytes (0.4 MiB) | 91,353 bytes | CC BY 4.0 |

## Forma recomendada: el script del curso

Desde la terminal del *Codespace*, en la raíz del repositorio:

```bash
python tools/descargar_datasets.py --lista              # muestra claves y URL
python tools/descargar_datasets.py diamonds             # uno
python tools/descargar_datasets.py adult wine           # varios
python tools/descargar_datasets.py todos --originales   # todos, más los ZIP oficiales del UCI
```

* Guarda cada uno como `data/proyecto/<clave>.csv`, con encabezados, y comprueba con *pandas* que se lee y que tiene las filas esperadas.
* `--originales` descarga además el ZIP del UCI y lo extrae en `data/proyecto/<clave>_originales/` (con la documentación `.names` o `Readme.txt`).
* `--forzar` vuelve a descargar aunque el archivo exista; `--destino` cambia la carpeta.
* Solo usa la biblioteca estándar y *pandas*: no hay que instalar nada más.

Desde un *notebook* (el 07 y la plantilla del proyecto ya traen esta celda), basta con elegir la clave:

```python
import os, sys
sys.path.insert(0, "tools")            # desde proyecto/, usa os.path.join(os.pardir, "tools")
from descargar_datasets import descargar
ruta = descargar("wine")               # → .../data/proyecto/wine.csv
```

## Fichas

### `diamonds`: precios de diamantes

* **Descripción:** precio (dólares) y atributos de 53,940 diamantes redondos: `carat` (peso en quilates), `cut`, `color` y `clarity` (categorías **ordinales**), `depth`, `table` y las dimensiones `x`, `y`, `z` en mm. Sin faltantes, pero 20 diamantes tienen alguna dimensión igual a 0 (imposible), algo que conviene auditar.
* **Fuente:** el conjunto `diamonds` del paquete de R *ggplot2* (<https://ggplot2.tidyverse.org/reference/diamonds.html>), redistribuido como CSV en [`mwaskom/seaborn-data`](https://github.com/mwaskom/seaborn-data), el repositorio que usa `sns.load_dataset()`.
* **Licencia:** *ggplot2* se distribuye con licencia MIT; `seaborn-data` no declara licencia propia y advierte que no es un archivo de datos de propósito general. Úsalo con fines educativos y cita *ggplot2*.
* **Cita:** Wickham, H. (2016). *ggplot2: Elegant Graphics for Data Analysis*. Springer-Verlag New York. Conjunto de datos `diamonds`.
* **URL:** <https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv>
* **Terminal:**
  ```bash
  mkdir -p data/proyecto
  curl -L -o data/proyecto/diamonds.csv https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv
  ```
* **Python:**
  ```python
  import seaborn as sns
  diamantes = sns.load_dataset("diamonds")   # cut, color y clarity llegan como category, pero SIN orden: defínelo tú
  # o bien, para tener el archivo local:
  diamantes = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv")
  ```

### `adult`: Adult / Census Income

* **Descripción:** 48,842 personas del censo de EE. UU. de 1994 con 14 atributos demográficos y laborales (`age`, `workclass`, `education`, `education-num`, `marital-status`, `occupation`, `relationship`, `race`, `sex`, `capital-gain`, `capital-loss`, `hours-per-week`, `native-country`, el peso muestral `fnlwgt`) y la variable `income` (`<=50K` / `>50K` dólares anuales).
* **Problemas de calidad conocidos** (parte de la auditoría, el script no los corrige): faltantes como `NaN` en `workclass` (963), `occupation` (966) y `native-country` (274), **y además** 4,262 celdas con el texto `"?"`; `income` tiene cuatro escrituras (`<=50K`, `<=50K.`, `>50K`, `>50K.`) porque une los archivos de entrenamiento y prueba originales.
* **Fuente:** UCI Machine Learning Repository, id 2: <https://archive.ics.uci.edu/dataset/2/adult>
* **Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0).
* **Cita:** Becker, B. y Kohavi, R. (1996). *Adult* [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5XW20>
* **URL:** CSV con encabezados <https://archive.ics.uci.edu/static/public/2/data.csv> · ZIP original (sin encabezados: `adult.data`, `adult.test`, `adult.names`) <https://archive.ics.uci.edu/static/public/2/adult.zip>
* **Terminal:**
  ```bash
  mkdir -p data/proyecto
  curl -L -o data/proyecto/adult.csv https://archive.ics.uci.edu/static/public/2/data.csv
  # ZIP original con la documentación:
  curl -L -o adult.zip https://archive.ics.uci.edu/static/public/2/adult.zip && unzip -o adult.zip -d data/proyecto/adult_originales && rm adult.zip
  ```
* **Python:**
  ```python
  adultos = pd.read_csv("https://archive.ics.uci.edu/static/public/2/data.csv")
  ```

### `bike`: Bike Sharing (rentas por hora)

* **Descripción:** 17,379 horas de rentas del sistema Capital Bikeshare (Washington, D. C.) del 1 de enero de 2011 al 31 de diciembre de 2012, con calendario (`dteday`, `season`, `yr`, `mnth`, `hr`, `holiday`, `weekday`, `workingday`), clima (`weathersit`; `temp`, `atemp`, `hum` y `windspeed` **normalizados** entre 0 y 1) y conteos (`casual`, `registered`, `cnt` = suma de ambos). Sin faltantes. El ZIP trae también `day.csv` (731 días).
* **Fuente:** UCI Machine Learning Repository, id 275: <https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset>
* **Licencia:** CC BY 4.0.
* **Cita:** Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C5W894> · Artículo: Fanaee-T, H. y Gama, J. (2013). Event labeling combining ensemble detectors and background knowledge. *Progress in Artificial Intelligence*, 1–15.
* **URL:** CSV (= `hour.csv`) <https://archive.ics.uci.edu/static/public/275/data.csv> · ZIP original (`hour.csv`, `day.csv`, `Readme.txt`) <https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip>
* **Terminal:**
  ```bash
  mkdir -p data/proyecto
  curl -L -o data/proyecto/bike.csv https://archive.ics.uci.edu/static/public/275/data.csv
  curl -L -o bike.zip "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip" && unzip -o bike.zip -d data/proyecto/bike_originales && rm bike.zip
  ```
* **Python:**
  ```python
  bicis = pd.read_csv("https://archive.ics.uci.edu/static/public/275/data.csv", parse_dates=["dteday"])
  ```

### `wine`: Wine Quality

* **Descripción:** 6,497 vinos portugueses *vinho verde* (1,599 tintos y 4,898 blancos) con 11 medidas fisicoquímicas (`fixed_acidity`, `volatile_acidity`, `citric_acid`, `residual_sugar`, `chlorides`, `free_sulfur_dioxide`, `total_sulfur_dioxide`, `density`, `pH`, `sulphates`, `alcohol`), la calificación sensorial `quality` (ordinal, observada de 3 a 9) y `color` (`red` / `white`). Sin faltantes; las clases de `quality` están muy desbalanceadas.
* **Fuente:** UCI Machine Learning Repository, id 186: <https://archive.ics.uci.edu/dataset/186/wine+quality>
* **Licencia:** CC BY 4.0.
* **Cita:** Cortez, P., Cerdeira, A., Almeida, F., Matos, T. y Reis, J. (2009). *Wine Quality* [Dataset]. UCI Machine Learning Repository. <https://doi.org/10.24432/C56S3T> · Artículo: Modeling wine preferences by data mining from physicochemical properties. *Decision Support Systems*, 47(4), 547–553.
* **URL:** CSV unificado con `color`, separado por comas <https://archive.ics.uci.edu/static/public/186/data.csv> · ZIP original (`winequality-red.csv` y `winequality-white.csv`, **separados por `;`**, más `winequality.names`) <https://archive.ics.uci.edu/static/public/186/wine+quality.zip>
* **Terminal:**
  ```bash
  mkdir -p data/proyecto
  curl -L -o data/proyecto/wine.csv https://archive.ics.uci.edu/static/public/186/data.csv
  curl -L -o wine.zip "https://archive.ics.uci.edu/static/public/186/wine+quality.zip" && unzip -o wine.zip -d data/proyecto/wine_originales && rm wine.zip
  ```
* **Python:**
  ```python
  vinos = pd.read_csv("https://archive.ics.uci.edu/static/public/186/data.csv")
  # archivos originales: pd.read_csv(ruta_tinto, sep=";")
  ```

## Alternativa opcional: `ucimlrepo`

El paquete oficial del UCI también funciona con *pandas* 3 (probado con `ucimlrepo` 0.0.7), pero **no** está en `requirements.txt` porque el script no lo necesita. Si quieres usarlo: `pip install ucimlrepo`.

```python
from ucimlrepo import fetch_ucirepo
adultos = fetch_ucirepo(id=2).data.original     # Bike Sharing: id=275 · Wine Quality: id=186
```

## Si no hay internet

1. **Si ya lo descargaste antes:** el archivo sigue en `data/proyecto/` mientras no borres el *Codespace*; el script y las celdas de los *notebooks* no lo vuelven a bajar.
2. **Desde otra computadora:** abre la URL del CSV en el navegador, guarda el archivo y arrástralo a la carpeta `data/proyecto/` en el explorador de archivos del *Codespace* (o clic derecho en la carpeta → **Upload...**). Nómbralo `<clave>.csv` (por ejemplo, `wine.csv`) para que las celdas lo encuentren.
3. **Sin ninguna de las dos:** la celda de descarga del 07 y de la plantilla avisa y carga `data/mpg.csv`, de modo que puedes avanzar con la estructura del análisis y cambiar al *dataset* real en cuanto tengas conexión. No entregues el proyecto con `mpg`.

Si la descarga falla con conexión, revisa la URL en la página del *dataset* (el UCI ha cambiado sus rutas en el pasado) y avisa al instructor.
