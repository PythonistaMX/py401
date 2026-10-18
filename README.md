# py401 · EDA Práctico

**Pythonista®** · Instructor: José Luis Chiquete · Nivel: intermedio-avanzado

Repositorio de trabajo del curso **Exploratory Data Analysis (EDA) Práctico**: 8 sesiones en vivo de 2 h (16 h), de lunes a jueves, de 6:30 a 8:30 pm (hora de la Ciudad de México), del 19 al 29 de octubre de 2026.

Herramientas: **NumPy, pandas, Matplotlib, Seaborn, SciPy y statsmodels**, en notebooks de Jupyter que corren en **GitHub Codespaces**. Las evaluaciones y el seguimiento se hacen en **Google Classroom**.

---

## 🚀 Cómo abrir el curso en Codespaces

1. Inicia sesión en GitHub y abre este repositorio (o tu copia/*fork*).
2. Haz clic en el botón verde **Code** → pestaña **Codespaces** → **Create codespace on main**.
3. Espera a que termine la configuración. **La primera vez tarda unos minutos** porque instala las librerías de `requirements.txt` (lo hace solo, con `postCreateCommand`).
4. En el explorador de la izquierda abre `notebooks/01_numpy_pandas_esenciales.ipynb`.
5. Arriba a la derecha, en **Select Kernel**, elige **Python Environments → Python 3.12** (`/usr/local/bin/python`).
6. Ejecuta las celdas en orden con `Shift + Enter`.

> 💡 Codespaces se detiene solo tras un rato de inactividad y tus cambios se conservan. Para no gastar tus horas gratuitas, detenlo al terminar: **github.com/codespaces** → `…` → **Stop codespace**.
>
> 💾 Antes de cada sesión, guarda tu trabajo con *commit* y *push* (pestaña **Source Control**) o descarga tu notebook.

### ¿Prefieres trabajar en tu computadora?

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
```

Se recomienda Python 3.11 o 3.12.

---

## 📁 Estructura

```
repo-py401/
├── .devcontainer/
│   └── devcontainer.json     # Configuración de Codespaces (Python 3.12 + extensiones Jupyter y Python)
├── data/                     # Datasets en CSV: el curso funciona sin internet
│   ├── penguins.csv          # Palmer Penguins: dataset principal (sesiones 1–6)
│   ├── titanic.csv           # Apoyo (sesiones 2 y 6)
│   ├── tips.csv              # Apoyo (sesión 4 y Evaluación 1)
│   ├── mpg.csv               # Demostración de EDA completo (sesión 7)
│   └── penguins_limpio.csv   # Versión limpia de penguins que genera el notebook 02 (se usa desde la sesión 3)
├── notebooks/                # Notebooks del alumno (sin resultados): uno por sesión
│   ├── 01_numpy_pandas_esenciales.ipynb
│   └── 02_calidad_y_faltantes.ipynb
├── soluciones/               # Versiones resueltas y ejecutadas (para el instructor)
├── requirements.txt          # Versiones fijas de las librerías
└── README.md
```

Los notebooks 03 a 08 se agregarán conforme avance el curso.

Los CSV provienen de [`mwaskom/seaborn-data`](https://github.com/mwaskom/seaborn-data), el repositorio que usa `sns.load_dataset()`. Diferencia importante: en el CSV de `penguins`, `sex` viene como `MALE`/`FEMALE`, mientras que `sns.load_dataset("penguins")` lo devuelve como `Male`/`Female`. El notebook 02 hace esa homologación.

---

## 🗓️ Calendario de sesiones

| # | Fecha | Módulo | Temas | Notebook |
|---|---|---|---|---|
| 1 | Lun 19 oct | I. Datos y su calidad | NumPy y pandas esenciales; tipos de variables; sesgos de recolección | `01_numpy_pandas_esenciales.ipynb` |
| 2 | Mar 20 oct | I. Datos y su calidad | Calidad de datos: duplicados, inconsistencias, valores faltantes | `02_calidad_y_faltantes.ipynb` |
| 3 | Mié 21 oct | II. Describir y comparar | Estadística descriptiva; forma de la distribución; outliers | `03_descriptiva_distribuciones.ipynb` |
| 4 | Jue 22 oct | II. Describir y comparar | Agregación; relaciones entre variables; correlación vs. causalidad; visualización efectiva | `04_agregacion_relaciones_visualizacion.ipynb` |
| 5 | Lun 26 oct | III. Inferencia estadística | Incertidumbre: muestreo, error estándar, intervalos de confianza, bootstrap | `05_incertidumbre_bootstrap.ipynb` |
| 6 | Mar 27 oct | III. Inferencia estadística | Pruebas t, proporciones, chi cuadrada, ANOVA; supuestos; tamaño del efecto | `06_pruebas_hipotesis_efecto.ipynb` |
| 7 | Mié 28 oct | IV. Proyecto integrador | EDA completo paso a paso | `07_eda_completo.ipynb` |
| 8 | Jue 29 oct | IV. Proyecto integrador | Redacción y presentación del informe de hallazgos | `08_informe_hallazgos.ipynb` |

Todas las sesiones son de **6:30 a 8:30 pm (CDMX)**.

### Evaluaciones

| Evaluación | Se publica | Cierra | Composición |
|---|---|---|---|
| Evaluación semanal 1 (Módulos I y II) | Jue 22 oct, 8:30 pm | Dom 25 oct, 11:59 pm | Cuestionario (40) + notebook (60) |
| Evaluación semanal 2 (Módulos III y IV) | Jue 29 oct, 8:30 pm | Dom 1 nov, 11:59 pm | Cuestionario (30) + Proyecto integrador (70) |

La consigna del Proyecto integrador se publica el lunes 26 de octubre.

**Diploma:** calificación final = (E1 + E2) / 2 **≥ 70** y asistencia a **al menos 7 de las 8 sesiones**. Entregas tardías: hasta 48 h con 10% de penalización.

---

## 🧭 Cómo están organizados los notebooks

- Cada notebook empieza con **objetivos** y la **agenda** de la sesión.
- Explicaciones en Markdown y código comentado que se ejecuta en orden.
- 🟢 **Ejercicios básicos**: lo que todos deben dominar.
- 🔴 **Retos opcionales**: para profundizar; ideales si ya tienes experiencia.
- Las celdas `# TU CÓDIGO AQUÍ` y **✍️ Tu respuesta** son para ti.
