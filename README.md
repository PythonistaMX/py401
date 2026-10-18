# Exploratory Data Analysis (EDA) Práctico (Py401)

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/codespaces)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg?style=for-the-badge)](LICENSE)
[![pandas](https://img.shields.io/badge/Datos-pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![statsmodels](https://img.shields.io/badge/Inferencia-statsmodels-4B8BBE?style=for-the-badge)](https://www.statsmodels.org/)

Este repositorio contiene el material oficial del curso **Py401 · Exploratory Data Analysis (EDA) Práctico** de **Pythonista®**, impartido por José Luis Chiquete. El curso enseña a explorar, describir y sacar conclusiones honestas de un conjunto de datos con *Python*, desde la auditoría de calidad hasta la inferencia estadística y el informe de hallazgos.

Página del curso: <https://www.pythonista.io/eventos/py401>

---

## 🗺️ Ruta de Aprendizaje

### Prerequisitos recomendados

Este curso asume conocimiento previo de *Python* y nociones básicas de *NumPy* y *pandas* (la sesión 1 las repasa).

| Curso | Título | Repositorio |
| :--- | :--- | :--- |
| Py101 | Introducción a la Programación con Python | [PythonistaMX/py101](https://github.com/PythonistaMX/py101) |
| Py311 | Fundamentos de Python para Ingeniería y Analítica de Datos | [PythonistaMX/py311](https://github.com/PythonistaMX/py311) |

---

## 🚀 Acerca del Curso

Un curso práctico de **8 sesiones en vivo de 2 horas** (16 horas) sobre notebooks de *Jupyter* que corren en **GitHub Codespaces**, con evaluaciones y seguimiento en **Google Classroom**. Al completarlo serás capaz de:

* **Auditar la calidad de los datos:** tipos de variables, duplicados, inconsistencias, valores faltantes y sesgos de recolección.
* **Describir distribuciones con criterio:** medidas robustas, forma de la distribución y valores atípicos.
* **Comparar grupos y medir relaciones:** agregaciones, correlación vs. causalidad y paradoja de Simpson.
* **Visualizar con eficacia:** elegir la gráfica correcta con *Matplotlib* y *Seaborn*.
* **Cuantificar la incertidumbre:** error estándar, intervalos de confianza y *bootstrap* con *SciPy* y *statsmodels*.
* **Contrastar hipótesis con responsabilidad:** supuestos, valor *p* y tamaño del efecto.
* **Comunicar hallazgos:** un EDA reproducible y un informe claro sobre sus límites.

Todo el entorno se ejecuta en la nube mediante **GitHub Codespaces**, sin necesidad de instalación local, y los datos de las sesiones vienen incluidos en `data/` (no se necesita internet para los notebooks). Solo el *dataset* del Proyecto integrador se descarga aparte (ver [Datasets del Proyecto integrador](#-datasets-del-proyecto-integrador)).

---

## 📅 Temario y Estructura

El curso consta de **8 sesiones de 2 horas**, de lunes a jueves de **6:30 a 8:30 pm (hora de la Ciudad de México)**, del 19 al 29 de octubre de 2026, divididas en 4 módulos:

| # | Fecha | Módulo | Temas | Notebook |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Lun 19 oct | I. Datos y su calidad | *NumPy* y *pandas* esenciales; tipos de variables; sesgos de recolección | [01](01_numpy_pandas_esenciales.ipynb) |
| 2 | Mar 20 oct | I. Datos y su calidad | Duplicados, inconsistencias y valores faltantes | [02](02_calidad_y_faltantes.ipynb) |
| 3 | Mié 21 oct | II. Describir y comparar | Estadística descriptiva; forma de la distribución; valores atípicos | [03](03_descriptiva_distribuciones.ipynb) |
| 4 | Jue 22 oct | II. Describir y comparar | Agregación; relaciones; correlación vs. causalidad; visualización efectiva | [04](04_agregacion_relaciones_visualizacion.ipynb) |
| 5 | Lun 26 oct | III. Inferencia estadística | Muestreo, error estándar, intervalos de confianza, *bootstrap* | [05](05_incertidumbre_bootstrap.ipynb) |
| 6 | Mar 27 oct | III. Inferencia estadística | Pruebas *t*, proporciones, chi cuadrada, ANOVA; supuestos; tamaño del efecto | [06](06_pruebas_hipotesis_efecto.ipynb) |
| 7 | Mié 28 oct | IV. Proyecto integrador | EDA completo paso a paso | [07](07_eda_completo.ipynb) |
| 8 | Jue 29 oct | IV. Proyecto integrador | Redacción y presentación del informe de hallazgos | [08](08_informe_hallazgos.ipynb) |

### Evaluaciones (en Google Classroom)

| Evaluación | Se publica | Cierra | Composición |
| :--- | :--- | :--- | :--- |
| Evaluación semanal 1 (Módulos I y II) | Jue 22 oct, 8:30 pm | Dom 25 oct, 11:59 pm | Cuestionario (40) + notebook (60) |
| Evaluación semanal 2 (Módulos III y IV) | Jue 29 oct, 8:30 pm | Dom 1 nov, 11:59 pm | Cuestionario (30) + Proyecto integrador (70) |

**Diploma:** calificación final = (E1 + E2) / 2 **≥ 70** y asistencia a **al menos 7 de las 8 sesiones**. Horarios en hora de la Ciudad de México.

### 📚 Contenidos

#### 🧭 Tabla de contenidos (enlaces rápidos)
- [01_numpy_pandas_esenciales.ipynb](01_numpy_pandas_esenciales.ipynb)
- [02_calidad_y_faltantes.ipynb](02_calidad_y_faltantes.ipynb)
- [03_descriptiva_distribuciones.ipynb](03_descriptiva_distribuciones.ipynb)
- [04_agregacion_relaciones_visualizacion.ipynb](04_agregacion_relaciones_visualizacion.ipynb)
- [05_incertidumbre_bootstrap.ipynb](05_incertidumbre_bootstrap.ipynb)
- [06_pruebas_hipotesis_efecto.ipynb](06_pruebas_hipotesis_efecto.ipynb)
- [07_eda_completo.ipynb](07_eda_completo.ipynb)
- [08_informe_hallazgos.ipynb](08_informe_hallazgos.ipynb)

#### 🔹 Módulo I: Datos y su calidad
* `01` - *NumPy* esencial (arreglos, `dtype`, vectorización, *broadcasting*, máscaras), *pandas* esencial (`info`, `describe`, `loc`/`iloc`, filtros, `assign`), tipos de variables (taxonomía, escalas de Stevens, `category`, tipos *nullable*, fechas), muestreo y sesgos de recolección.
* `02` - Lista de verificación de calidad, duplicados exactos y por llave, inconsistencias, mecanismos de faltantes (MCAR, MAR, MNAR) e imputación; genera `data/penguins_limpio.csv`.

#### 🔹 Módulo II: Describir y comparar
* `03` - Tendencia central y dispersión, forma de la distribución (histograma, KDE, ECDF, *boxplot*) y valores atípicos (IQR, *z* robusto).
* `04` - `groupby`/`agg`, `pivot_table`, `crosstab`, `melt`; Pearson y Spearman; paradoja de Simpson; visualización efectiva.

#### 🔹 Módulo III: Inferencia estadística
* `05` - Distribución muestral (ley de los grandes números, teorema central del límite, tamaño de muestra y diseño estratificado), error estándar, intervalos de confianza y *bootstrap* (`scipy.stats`, *statsmodels*).
* `06` - *t* de Welch, Mann-Whitney, permutación, proporciones, chi cuadrada, ANOVA y Tukey; tamaño del efecto.

#### 🔹 Módulo IV: Proyecto integrador
* `07` - EDA completo y reproducible sobre `mpg`; arranque del proyecto.
* `08` - Informe de hallazgos y exportación con `nbconvert`.

Materiales de evaluación:

* `evaluaciones/eval1_eda_descriptivo.ipynb` - Consigna, rúbrica y esqueleto del *notebook* de la Evaluación semanal 1 (`tips`).
* `proyecto/plantilla_proyecto_integrador.ipynb` - Plantilla del Proyecto integrador (Evaluación semanal 2), con la estructura del EDA y del informe; descarga el *dataset* elegido a `data/proyecto/` y corre completa con `mpg.csv` mientras no se elija uno.

> **📝 Nota:** Cada notebook incluye ejercicios básicos 🟢 y retos opcionales 🔴. Las celdas `# TU CÓDIGO AQUÍ` y **✍️ Tu respuesta** son para ti. Las versiones resueltas están en `soluciones/` (`NN_..._soluciones.ipynb`).

#### 📁 Datos (`data/`)
* `penguins.csv` - Palmer Penguins, dataset principal (sesiones 1–6).
* `penguins_limpio.csv` - versión limpia que genera el notebook 02 (desde la sesión 3).
* `titanic.csv` - apoyo (sesiones 2 y 6).
* `tips.csv` - apoyo (sesión 4 y Evaluación 1).
* `mpg.csv` - demostración de EDA completo (sesión 7).

Los CSV provienen de [`mwaskom/seaborn-data`](https://github.com/mwaskom/seaborn-data), el repositorio que usa `sns.load_dataset()`. En el CSV de `penguins`, `sex` viene como `MALE`/`FEMALE` (en `sns.load_dataset("penguins")` es `Male`/`Female`); el notebook 02 hace esa homologación.

#### 📦 Datasets del Proyecto integrador

Los *datasets* del proyecto **no** vienen en el repositorio: se descargan a `data/proyecto/` (carpeta ignorada por *git*). Fichas completas (fuente, licencia, cita, columnas, problemas de calidad conocidos y comandos alternativos) en [`data/DATASETS.md`](data/DATASETS.md).

| Clave | *Dataset* | Filas × columnas | Tamaño del CSV | Fuente | Licencia |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `diamonds` | Precios de diamantes | 53,940 × 10 | 2.6 MiB | [*ggplot2*](https://ggplot2.tidyverse.org/reference/diamonds.html) vía [`seaborn-data`](https://github.com/mwaskom/seaborn-data) | MIT (*ggplot2*) |
| `adult` | Adult / Census Income | 48,842 × 15 | 5.1 MiB | [UCI, id 2](https://archive.ics.uci.edu/dataset/2/adult) | CC BY 4.0 |
| `bike` | Bike Sharing (por hora) | 17,379 × 17 | 1.1 MiB | [UCI, id 275](https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset) | CC BY 4.0 |
| `wine` | Wine Quality (tinto + blanco) | 6,497 × 13 | 0.4 MiB | [UCI, id 186](https://archive.ics.uci.edu/dataset/186/wine+quality) | CC BY 4.0 |

Desde la terminal del *Codespace*, en la raíz del repositorio (solo usa la biblioteca estándar y *pandas*):

```bash
python tools/descargar_datasets.py --lista              # claves y URL
python tools/descargar_datasets.py wine                 # uno o varios: diamonds adult bike wine
python tools/descargar_datasets.py todos --originales   # todos, más los ZIP oficiales del UCI
```

El notebook `07` y la plantilla del proyecto traen una celda que hace lo mismo con solo escribir la clave en `DATASET_PROYECTO`. **Sin internet:** sube el CSV descargado en otra computadora a `data/proyecto/<clave>.csv` desde el explorador del *Codespace*; si no hay archivo ni conexión, las celdas avisan y usan `mpg.csv` para que puedas seguir trabajando.

---

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales! Este repositorio está configurado para **GitHub Codespaces**.

1. Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2. Ve a la pestaña **"Codespaces"**.
3. Haz clic en **"Create codespace on main"**.

El entorno se iniciará automáticamente con:
* *Python* 3.12
* Extensiones de *Python* y *Jupyter* para VS Code
* Todas las librerías del curso instaladas según las versiones mínimas de `requirements.txt`: *NumPy*, *pandas*, *Matplotlib*, *Seaborn*, *SciPy* y *statsmodels*.

> ⚠️ **ADVERTENCIA: el curso usa *pandas* 3.** *pandas* 3.0 (enero de 2026) es una gran actualización de arquitectura: Copy-on-Write es obligatorio y el texto se guarda por defecto con el tipo `str` respaldado por PyArrow. Es **incompatible hacia atrás**: código escrito para *pandas* 2.x (asignación encadenada como `df["col"][fila] = valor`, `inplace=True` sobre una columna, comprobaciones de `dtype == object` para texto) puede cambiar de comportamiento o fallar sin error visible. El notebook `01` lo explica con ejemplos; consulta también las [notas de versión de *pandas* 3.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html). Si instalas el entorno por tu cuenta, usa `requirements.txt` (requiere *pandas* ≥ 3.0 y *PyArrow* ≥ 16).

La primera vez tarda unos minutos porque instala las librerías. Después abre `01_numpy_pandas_esenciales.ipynb`, elige el kernel **Python 3.12** (`/usr/local/bin/python`) en **Select Kernel** y ejecuta las celdas en orden con `Shift + Enter`.

> 💡 Codespaces se detiene solo tras un rato de inactividad y tus cambios se conservan. Para no gastar tus horas gratuitas, detenlo al terminar: **github.com/codespaces** → `…` → **Stop codespace**.

### Ejecución Local (Opcional)
Si prefieres trabajar en tu máquina:

```bash
# Clonar el repositorio
git clone https://github.com/PythonistaMX/py401.git
cd py401

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar Jupyter
jupyter lab
```

---

## 📖 Recursos Adicionales

* [Documentación oficial de pandas](https://pandas.pydata.org/docs/)
* [Documentación oficial de Seaborn](https://seaborn.pydata.org/)
* [Documentación oficial de SciPy (`scipy.stats`)](https://docs.scipy.org/doc/scipy/reference/stats.html)
* [Documentación oficial de statsmodels](https://www.statsmodels.org/stable/)

---

## 📝 Licencia

Este proyecto está bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC-BY 4.0)**.

**Eres libre de:**
- ✅ Compartir el material en cualquier medio o formato
- ✅ Adaptar, remezclar y crear contenido derivado
- ✅ Usar con fines comerciales

**Con la condición de:**
- 📌 **Atribución:** Debes dar crédito apropiado, proporcionar un enlace a la licencia e indicar si se han realizado cambios.

Para más información, visita: https://creativecommons.org/licenses/by/4.0/

Véase el archivo [LICENSE](LICENSE) para los términos completos.

&copy; José Luis Chiquete Valdivieso. 2017-2026.
