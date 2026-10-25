# Exploratory Data Analysis (EDA) Práctico (Py401)

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://codespaces.new/PythonistaMX/py401)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg?style=for-the-badge)](LICENSE)
[![pandas](https://img.shields.io/badge/Datos-pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![statsmodels](https://img.shields.io/badge/Inferencia-statsmodels-4B8BBE?style=for-the-badge)](https://www.statsmodels.org/)

Este repositorio contiene el material oficial del curso **Py401 · Exploratory Data Analysis (EDA) Práctico** de **Pythonista®**, impartido por José Luis Chiquete. El curso enseña a explorar, describir y sacar conclusiones honestas de un conjunto de datos con *Python*, desde la auditoría de calidad hasta la inferencia estadística y el informe de hallazgos.

Página del curso: <https://www.pythonista.io/eventos/py401>

---

## 🗺️ Ruta de Aprendizaje

### Prerequisitos recomendados

Este curso asume conocimiento previo de *Python* y nociones básicas de *NumPy* y *pandas* (los notebooks `02` y `03` las repasan).

| Curso | Título | Repositorio |
| :--- | :--- | :--- |
| Py101 | Introducción a la Programación con Python | [PythonistaMX/py101](https://github.com/PythonistaMX/py101) |
| Py311 | Fundamentos de Python para Ingeniería y Analítica de Datos | [PythonistaMX/py311](https://github.com/PythonistaMX/py311) |

---

## 🚀 Acerca del Curso

Un curso práctico de **8 sesiones en vivo de 2 horas** (16 horas) sobre notebooks de *Jupyter* que corren en **GitHub Codespaces**, con práctica y dudas en **Google Classroom**. Al completarlo serás capaz de:

* **Auditar la calidad de los datos:** tipos de variables, duplicados, inconsistencias, valores faltantes y sesgos de recolección.
* **Describir distribuciones con criterio:** medidas robustas, forma de la distribución y valores atípicos.
* **Comparar grupos y medir relaciones:** agregaciones, correlación vs. causalidad y paradoja de Simpson.
* **Visualizar con eficacia:** elegir la gráfica correcta con *Matplotlib* y *Seaborn*.
* **Cuantificar la incertidumbre:** error estándar, intervalos de confianza y *bootstrap* con *SciPy* y *statsmodels*.
* **Contrastar hipótesis con responsabilidad:** supuestos, valor *p* y tamaño del efecto.
* **Comunicar hallazgos:** un EDA reproducible y un informe claro sobre sus límites.

Todo el entorno se ejecuta en la nube mediante **GitHub Codespaces**, sin necesidad de instalación local, y los datos de las sesiones vienen incluidos en `data/` (no se necesita internet para los notebooks).

---

## 📅 Temario y Estructura

El curso consta de **8 sesiones en vivo de 2 horas**, divididas en 4 módulos. Los *notebooks* se numeran por tema y cada sesión abarca varios (la correspondencia entre sesiones y *notebooks* está en [`INSTRUCTOR_GUIDE.md`](INSTRUCTOR_GUIDE.md)).

| Módulo | Temas | Notebooks |
| :--- | :--- | :--- |
| I. Datos y su calidad | *NumPy* y *pandas* esenciales; tipos de variables; sesgos de recolección; duplicados, inconsistencias y valores faltantes | `01`-`09` |
| II. Describir y comparar | Estadística descriptiva; forma de la distribución; valores atípicos; agregación; relaciones; correlación vs. causalidad; visualización efectiva | `10`-`15` |
| III. Inferencia estadística | Muestreo, error estándar, intervalos de confianza, *bootstrap*; pruebas *t*, proporciones, chi cuadrada, ANOVA; supuestos; tamaño del efecto | `16`-`22` |
| IV. Del análisis al informe | EDA completo paso a paso; reproducibilidad; redacción y comunicación del informe de hallazgos | `23`-`26` |

### Práctica y diploma

* Los *notebooks* son **práctica**: los ejercicios 🟢 y los retos 🔴 se trabajan en clase y en Google Classroom, que también es el canal de dudas.
* `15_visualizacion_efectiva.ipynb` cierra el Módulo II con una **práctica integradora** con `tips`, y `26_del_notebook_al_informe.ipynb` cierra el curso con **preguntas de repaso** de los Módulos III y IV.

**Diploma:** requiere asistencia a **al menos 7 de las 8 sesiones** (80%; se permite como máximo una falta).

### 📚 Contenidos

#### 🧭 Tabla de contenidos (enlaces rápidos)
- [01_bienvenida_y_reglas_del_curso.ipynb](01_bienvenida_y_reglas_del_curso.ipynb)
- [02_numpy_esencial.ipynb](02_numpy_esencial.ipynb)
- [03_pandas_3_esencial.ipynb](03_pandas_3_esencial.ipynb)
- [04_tipos_de_variables.ipynb](04_tipos_de_variables.ipynb)
- [05_muestreo_y_sesgos_de_recoleccion.ipynb](05_muestreo_y_sesgos_de_recoleccion.ipynb)
- [06_diccionario_de_datos.ipynb](06_diccionario_de_datos.ipynb)
- [07_duplicados_e_inconsistencias.ipynb](07_duplicados_e_inconsistencias.ipynb)
- [08_valores_faltantes.ipynb](08_valores_faltantes.ipynb)
- [09_auditoria_de_calidad.ipynb](09_auditoria_de_calidad.ipynb)
- [10_tendencia_central_y_dispersion.ipynb](10_tendencia_central_y_dispersion.ipynb)
- [11_forma_de_la_distribucion.ipynb](11_forma_de_la_distribucion.ipynb)
- [12_valores_atipicos_y_transformaciones.ipynb](12_valores_atipicos_y_transformaciones.ipynb)
- [13_agregacion.ipynb](13_agregacion.ipynb)
- [14_relaciones_entre_variables.ipynb](14_relaciones_entre_variables.ipynb)
- [15_visualizacion_efectiva.ipynb](15_visualizacion_efectiva.ipynb)
- [16_distribucion_muestral.ipynb](16_distribucion_muestral.ipynb)
- [17_error_estandar_e_intervalos_de_confianza.ipynb](17_error_estandar_e_intervalos_de_confianza.ipynb)
- [18_bootstrap_e_interpretacion_de_intervalos.ipynb](18_bootstrap_e_interpretacion_de_intervalos.ipynb)
- [19_logica_del_contraste.ipynb](19_logica_del_contraste.ipynb)
- [20_pruebas_para_dos_grupos.ipynb](20_pruebas_para_dos_grupos.ipynb)
- [21_proporciones_y_mas_de_dos_grupos.ipynb](21_proporciones_y_mas_de_dos_grupos.ipynb)
- [22_tamano_del_efecto.ipynb](22_tamano_del_efecto.ipynb)
- [23_eda_completo_con_mpg.ipynb](23_eda_completo_con_mpg.ipynb)
- [24_reproducibilidad_de_un_eda.ipynb](24_reproducibilidad_de_un_eda.ipynb)
- [25_estructura_del_informe_y_comunicacion.ipynb](25_estructura_del_informe_y_comunicacion.ipynb)
- [26_del_notebook_al_informe.ipynb](26_del_notebook_al_informe.ipynb)

#### 🔹 Módulo I: Datos y su calidad
* `01` - Bienvenida, reglas del curso (asistencia y diploma); arranque del *Codespace*.
* `02` - *NumPy* esencial: arreglos, `dtype`, vectorización, *broadcasting*, máscaras y decisiones que cambian resultados (`ddof`, `NaN`, desbordamiento, flotantes).
* `03` - *pandas* 3 esencial: *Copy-on-Write*, tipo `str`, `read_csv`, `info`, `describe`, `loc`/`iloc`, filtros, `assign` y faltantes silenciosos.
* `04` - Tipos de variables: taxonomía, escalas de Stevens, `dtype` de *pandas* 3, `category`, tipos *nullable* y fechas.
* `05` - Muestreo (población, marco, parámetro y estadístico; diseños comparados por simulación) y sesgos de recolección.
* `06` - Ejercicio guiado: diccionario de datos de `penguins`.
* `07` - Lista de verificación de calidad, duplicados exactos y por llave, inconsistencias de texto, categorías, rangos, centinelas y unidades.
* `08` - Mecanismos de faltantes (MCAR, MAR, MNAR), perfil de faltantes, tratamiento e imputación y su efecto.
* `09` - Auditoría de calidad de `titanic` y `penguins`; genera `data/penguins_limpio.csv`.

#### 🔹 Módulo II: Describir y comparar
* `10` - Tendencia central y dispersión: medidas clásicas y robustas (mediana, IQR, MAD).
* `11` - Forma de la distribución: asimetría, curtosis, multimodalidad; histograma, KDE, ECDF y *boxplot*.
* `12` - Valores atípicos (IQR, *z*, *z* robusto), ¿error o valor real?, transformación logarítmica y ejercicio integrador.
* `13` - Agregación: `groupby`/`agg`, `pivot_table`, `crosstab` y `melt`.
* `14` - Relaciones entre variables: Pearson y Spearman, correlación vs. causalidad, confusores y paradoja de Simpson.
* `15` - Visualización efectiva con *Matplotlib* y *Seaborn*, ejercicio de la sesión y práctica integradora con `tips`.

#### 🔹 Módulo III: Inferencia estadística
* `16` - Distribución muestral: ley de los grandes números, teorema central del límite, tamaño de muestra y diseño estratificado.
* `17` - Error estándar e intervalos de confianza para medias y proporciones (Wald, Wilson, Clopper-Pearson); cobertura.
* `18` - *Bootstrap* (`scipy.stats.bootstrap`) e interpretación correcta de un IC.
* `19` - Lógica del contraste: H0/H1, valor *p*, errores tipo I y II, potencia.
* `20` - Dos grupos: *t* de Student y de Welch, Mann-Whitney y permutación.
* `21` - Proporciones y chi cuadrada; más de dos grupos: Levene, ANOVA, Welch y Tukey; comparaciones múltiples.
* `22` - Tamaño del efecto: d de Cohen, V de Cramér y η².

#### 🔹 Módulo IV: Del análisis al informe
* `23` - EDA completo y reproducible sobre `mpg`, paso a paso.
* `24` - Reproducibilidad de un EDA: *Restart & Run All*, semillas, rutas relativas, funciones reutilizables y `requirements.txt`, aplicados a `mpg`.
* `25` - Estructura del informe de hallazgos; comunicar IC y tamaños del efecto en lenguaje llano; gráfica final; qué no afirmar.
* `26` - Del *notebook* al informe con `nbconvert`, taller de redacción y revisión entre pares, preguntas de repaso y cierre del curso.

> **📝 Nota:** Los notebooks con práctica incluyen ejercicios básicos 🟢 y retos opcionales 🔴. Las celdas `# TU CÓDIGO AQUÍ` y **✍️ Tu respuesta** son para ti. Las versiones resueltas están en `soluciones/` (`NN_..._soluciones.ipynb`); `01`, `23` y `25` no tienen ejercicios. Cada notebook es independiente y se puede abrir y ejecutar por separado.

#### 📁 Datos (`data/`)
* `penguins.csv` - Palmer Penguins, dataset principal (notebooks `03` a `22`).
* `penguins_limpio.csv` - versión limpia que genera `09_auditoria_de_calidad.ipynb` (se usa desde `10`; si falta, cada notebook la regenera).
* `titanic.csv` - apoyo (calidad, proporciones e inferencia).
* `tips.csv` - apoyo (agregación, relaciones, pruebas y práctica integradora del `15`).
* `mpg.csv` - demostración de EDA completo (`23`) y práctica de reproducibilidad (`24`).

Los CSV provienen de [`mwaskom/seaborn-data`](https://github.com/mwaskom/seaborn-data), el repositorio que usa `sns.load_dataset()`. En el CSV de `penguins`, `sex` viene como `MALE`/`FEMALE` (en `sns.load_dataset("penguins")` es `Male`/`Female`); `09_auditoria_de_calidad.ipynb` hace esa homologación.

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

> ⚠️ **ADVERTENCIA: el curso usa *pandas* 3.** *pandas* 3.0 es una gran actualización de arquitectura: Copy-on-Write es obligatorio y el texto se guarda por defecto con el tipo `str` respaldado por PyArrow. Es **incompatible hacia atrás**: código escrito para *pandas* 2.x (asignación encadenada como `df["col"][fila] = valor`, `inplace=True` sobre una columna, comprobaciones de `dtype == object` para texto) puede cambiar de comportamiento o fallar sin error visible. El notebook `03_pandas_3_esencial.ipynb` lo explica con ejemplos; consulta también las [notas de versión de *pandas* 3.0](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html). Si instalas el entorno por tu cuenta, usa `requirements.txt` (requiere *pandas* ≥ 3.0 y *PyArrow* ≥ 16).

La primera vez tarda unos minutos porque instala las librerías. Después abre `01_bienvenida_y_reglas_del_curso.ipynb`, elige el kernel **Python 3.12** (`/usr/local/bin/python`) en **Select Kernel** y ejecuta las celdas en orden con `Shift + Enter`.

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
