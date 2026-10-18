# Instructor Guide - Py401

Guía operativa para impartir **Py401 · EDA Práctico** con consistencia técnica y pedagógica. Fuente: mapa de sesiones del curso. Las fechas y los horarios de cada edición se publican en Google Classroom y en la página del curso; este repositorio no los fija para que el material sirva en cualquier edición.

## Estructura (8 sesiones de 2 horas, 26 *notebooks*)

Los *notebooks* se numeran por tema, en orden, a lo largo de todo el curso; cada sesión abarca varios. Esta es la única tabla que relaciona sesiones y *notebooks*:

1. Sesión 1: *NumPy* y *pandas* esenciales, tipos de variables y sesgos de recolección (01-06).
2. Sesión 2: calidad de datos y valores faltantes (07-09). Genera `data/penguins_limpio.csv` (`09`).
3. Sesión 3: estadística descriptiva, forma de la distribución y valores atípicos (10-12).
4. Sesión 4: agregación, relaciones entre variables y visualización efectiva (13-15). Se publica la Evaluación semanal 1.
5. Sesión 5: incertidumbre, intervalos de confianza y *bootstrap* (16-18). Se publica la consigna del Proyecto integrador.
6. Sesión 6: pruebas de hipótesis y tamaño del efecto (19-22).
7. Sesión 7: EDA completo paso a paso con `mpg` y arranque del proyecto (23-24).
8. Sesión 8: informe de hallazgos y presentación (25-26). Se publica la Evaluación semanal 2.

Cada *notebook* es independiente: tiene su propia celda de preparación (bibliotecas, `DATA` con `os.path.join` y semilla `401`) y, cuando necesita algo de un *notebook* anterior, lo vuelve a crear en la celda "Objetos de los *notebooks* anteriores". Los temas con ejercicios tienen su versión resuelta en `soluciones/NN_tema_soluciones.ipynb`; `01`, `23` y `25` no tienen ejercicios ni soluciones.

## Objetivos y agenda por sesión

En las agendas, las subsecciones marcadas con 📖 **Lectura opcional** se revisan en casa. Los ejercicios 🟢 que no alcancen a resolverse en clase quedan como práctica; los retos 🔴 son siempre opcionales.

### Sesión 1 · Módulo I: Datos y su calidad

**Notebooks:** [`01_bienvenida_y_reglas_del_curso`](01_bienvenida_y_reglas_del_curso.ipynb), [`02_numpy_esencial`](02_numpy_esencial.ipynb), [`03_pandas_3_esencial`](03_pandas_3_esencial.ipynb), [`04_tipos_de_variables`](04_tipos_de_variables.ipynb), [`05_muestreo_y_sesgos_de_recoleccion`](05_muestreo_y_sesgos_de_recoleccion.ipynb), [`06_diccionario_de_datos`](06_diccionario_de_datos.ipynb).

**Descripción:** En esta sesión se repasarán los fundamentos de *NumPy* y *pandas*, se clasificarán las variables por su tipo y por la forma en que se recolectaron, y se presentarán los cambios de *pandas* 3 que afectan al resto del curso.

**Objetivo:** Cargar y explorar un *dataframe* con soltura, y **clasificar cada variable por su tipo y por cómo se recolectó**.

Al terminar, el participante podrá:
1. Usar arreglos de *NumPy*: `dtype`, operaciones vectorizadas, *broadcasting* y máscaras booleanas.
2. Leer y explorar datos con *pandas* 3: `info`, `describe`, `loc`/`iloc`, filtros y `assign`.
3. Distinguir variables numéricas (continuas/discretas), categóricas (nominales/ordinales) y fechas, y representarlas con el `dtype` correcto (`str`, `category`, tipos *nullable*).
4. Reconocer sesgos de recolección: selección, supervivencia, no respuesta y medición.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Bienvenida, reglas de evaluación y asistencia, arranque del *Codespace* | `01_bienvenida_y_reglas_del_curso` |
| 15 | *NumPy*: repaso exprés y decisiones que cambian resultados | `02_numpy_esencial` |
| 25 | *pandas*: repaso exprés, *pandas* 3 y decisiones al explorar | `03_pandas_3_esencial` |
| 25 | Tipos de variables: taxonomía, escalas de medición y `dtype` | `04_tipos_de_variables` |
| 30 | Muestreo y sesgos de recolección | `05_muestreo_y_sesgos_de_recoleccion` |
| 15 | Ejercicio guiado (diccionario de datos) y cierre | `06_diccionario_de_datos` |

### Sesión 2 · Módulo I: Datos y su calidad

**Notebooks:** [`07_duplicados_e_inconsistencias`](07_duplicados_e_inconsistencias.ipynb), [`08_valores_faltantes`](08_valores_faltantes.ipynb), [`09_auditoria_de_calidad`](09_auditoria_de_calidad.ipynb).

**Descripción:** En esta sesión se auditará la calidad de un *dataset* (duplicados, inconsistencias de texto, rangos imposibles y unidades), se perfilarán los mecanismos de faltantes (MCAR, MAR, MNAR) y se compararán estrategias de tratamiento y su efecto en las distribuciones, usando `titanic` y `penguins`. Al final se genera `data/penguins_limpio.csv`.

**Objetivo:** **Auditar la calidad de un *dataset* y elegir de forma justificada cómo tratar los faltantes.**

Al terminar, el participante podrá:
1. Aplicar una lista de verificación de calidad a cualquier *dataset*.
2. Detectar y resolver duplicados exactos y por llave.
3. Corregir inconsistencias de texto, categorías mal escritas, rangos imposibles y unidades.
4. Distinguir los mecanismos de faltantes (MCAR, MAR, MNAR) y perfilarlos.
5. Comparar eliminación, imputación simple, imputación por grupo e indicador de faltante, y medir su efecto en las distribuciones.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Repaso y lista de verificación de calidad | `07_duplicados_e_inconsistencias` |
| 20 | Duplicados: exactos y por llave | `07_duplicados_e_inconsistencias` |
| 25 | Inconsistencias: texto, categorías, rangos imposibles, unidades | `07_duplicados_e_inconsistencias` |
| 15 | Mecanismos de faltantes y cómo perfilarlos | `08_valores_faltantes` |
| 30 | Tratamiento de faltantes y su efecto en las distribuciones | `08_valores_faltantes` |
| 20 | Ejercicio (`titanic` + `penguins`) y cierre | `09_auditoria_de_calidad` |

### Sesión 3 · Módulo II: Describir y comparar

**Notebooks:** [`10_tendencia_central_y_dispersion`](10_tendencia_central_y_dispersion.ipynb), [`11_forma_de_la_distribucion`](11_forma_de_la_distribucion.ipynb), [`12_valores_atipicos_y_transformaciones`](12_valores_atipicos_y_transformaciones.ipynb).

**Descripción:** En esta sesión se describirán distribuciones con medidas clásicas y robustas (media, mediana, desviación estándar, IQR y MAD), se analizará su forma (asimetría, curtosis y multimodalidad) con histogramas, KDE, ECDF y diagramas de caja, y se detectarán valores atípicos con la regla del IQR y el puntaje *z* robusto, usando `penguins_limpio`.

**Objetivo:** **Describir distribuciones con medidas robustas y detectar valores atípicos sin eliminarlos por reflejo.**

Al terminar, el participante podrá:
1. Calcular e interpretar media, mediana, desviación estándar, IQR y MAD, y saber cuáles son robustas.
2. Describir la forma de una distribución (asimetría, curtosis, multimodalidad) y elegir la gráfica adecuada: histograma, KDE, ECDF o diagrama de caja.
3. Detectar valores atípicos con la regla del IQR, el puntaje *z* y el puntaje *z* robusto, y decidir si son errores o valores reales.
4. Aplicar una transformación logarítmica y explicar su efecto.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Repaso: `penguins_limpio` | `10_tendencia_central_y_dispersion` |
| 25 | Tendencia central y dispersión | `10_tendencia_central_y_dispersion` |
| 25 | Forma de la distribución | `11_forma_de_la_distribucion` |
| 25 | Valores atípicos | `12_valores_atipicos_y_transformaciones` |
| 15 | Transformaciones (log) | `12_valores_atipicos_y_transformaciones` |
| 20 | Ejercicio integrador y cierre | `12_valores_atipicos_y_transformaciones` |

### Sesión 4 · Módulo II: Describir y comparar

**Notebooks:** [`13_agregacion`](13_agregacion.ipynb), [`14_relaciones_entre_variables`](14_relaciones_entre_variables.ipynb), [`15_visualizacion_efectiva`](15_visualizacion_efectiva.ipynb).

**Descripción:** En esta sesión se resumirán datos por grupos (`groupby`, `pivot_table`, `crosstab`, `melt`), se medirán relaciones entre variables con las correlaciones de Pearson y Spearman sin confundir correlación con causalidad (confusores y paradoja de Simpson) y se construirán gráficas claras con *Matplotlib* y *Seaborn*. Al final se presenta la **Evaluación semanal 1**.

**Objetivo:** **Resumir por grupos, medir relaciones entre variables y comunicarlas con gráficas claras, sin confundir correlación con causalidad.**

Al terminar, el participante podrá:
1. Agregar con `groupby`/`agg`, `pivot_table` y `crosstab`, y cambiar entre formato ancho y largo con `melt`.
2. Calcular e interpretar las correlaciones de Pearson y Spearman y leer tablas de contingencia.
3. Reconocer confusores y la paradoja de Simpson.
4. Elegir la gráfica adecuada y cuidar escalas, facetas, color y anotaciones.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Repaso | `13_agregacion` |
| 25 | Agregación | `13_agregacion` |
| 25 | Relaciones entre variables | `14_relaciones_entre_variables` |
| 30 | Visualización efectiva | `15_visualizacion_efectiva` |
| 20 | Ejercicio de la sesión | `15_visualizacion_efectiva` |
| 10 | Presentación de la Evaluación semanal 1 | `15_visualizacion_efectiva` |

### Sesión 5 · Módulo III: Inferencia estadística

**Notebooks:** [`16_distribucion_muestral`](16_distribucion_muestral.ipynb), [`17_error_estandar_e_intervalos_de_confianza`](17_error_estandar_e_intervalos_de_confianza.ipynb), [`18_bootstrap_e_interpretacion_de_intervalos`](18_bootstrap_e_interpretacion_de_intervalos.ipynb).

**Descripción:** En esta sesión se cuantificará la incertidumbre de una estimación: se simulará la distribución muestral con *NumPy*, se calcularán errores estándar e intervalos de confianza para medias y proporciones con *SciPy* y *statsmodels*, y se construirán intervalos *bootstrap* con `scipy.stats.bootstrap`, usando `penguins`. Al final se presenta la consigna del **Proyecto integrador**.

**Objetivo:** **Acompañar cada estimación con su incertidumbre, con fórmulas clásicas y con remuestreo, e interpretarla correctamente.**

Al terminar, el participante podrá:
1. Explicar la distribución muestral, la ley de los grandes números y el teorema central del límite, y cómo el tamaño de muestra y el diseño (estratificado o aleatorio simple) cambian el error estándar.
2. Calcular intervalos de confianza para una media (fórmula *t*) y para una proporción (Wald, Wilson, Clopper-Pearson).
3. Construir intervalos *bootstrap* para la media, la mediana y la diferencia entre dos grupos.
4. Interpretar un intervalo de confianza sin las confusiones más comunes y elegir el método según los datos.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Retroalimentación de la Evaluación semanal 1 | `16_distribucion_muestral` |
| 30 | Distribución muestral: ley de los grandes números, teorema central del límite, tamaño de muestra y diseño | `16_distribucion_muestral` |
| 25 | Error estándar e intervalos de confianza | `17_error_estandar_e_intervalos_de_confianza` |
| 25 | *Bootstrap* | `18_bootstrap_e_interpretacion_de_intervalos` |
| 15 | Interpretación correcta de un IC y consigna del Proyecto integrador | `18_bootstrap_e_interpretacion_de_intervalos` |
| 20 | Ejercicio de la sesión y cierre | `18_bootstrap_e_interpretacion_de_intervalos` |

### Sesión 6 · Módulo III: Inferencia estadística

**Notebooks:** [`19_logica_del_contraste`](19_logica_del_contraste.ipynb), [`20_pruebas_para_dos_grupos`](20_pruebas_para_dos_grupos.ipynb), [`21_proporciones_y_mas_de_dos_grupos`](21_proporciones_y_mas_de_dos_grupos.ipynb), [`22_tamano_del_efecto`](22_tamano_del_efecto.ipynb).

**Descripción:** En esta sesión se aplicarán pruebas *t* de Student y de Welch, Mann-Whitney, pruebas por permutación, la prueba *z* de proporciones, la chi cuadrada de independencia y el ANOVA de una vía con Levene, Welch y Tukey, siempre acompañadas del tamaño del efecto (d de Cohen, V de Cramér y η²), usando `penguins`, `titanic` y `tips`.

**Objetivo:** **Elegir la prueba adecuada, revisar sus supuestos e informar el tamaño del efecto junto con el valor *p*.**

Al terminar, el participante podrá:
1. Explicar H0/H1, el valor *p*, los errores tipo I y II, la potencia y el riesgo de las comparaciones múltiples.
2. Comparar dos grupos con *t* de Welch, Mann-Whitney o permutación, según los datos.
3. Probar proporciones y la independencia de dos variables categóricas.
4. Comparar más de dos grupos con ANOVA, revisar la igualdad de varianzas y localizar diferencias con Tukey.
5. Reportar d de Cohen, V de Cramér y η², e interpretar su magnitud.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Repaso | `19_logica_del_contraste` |
| 20 | La lógica del contraste | `19_logica_del_contraste` |
| 25 | Dos grupos | `20_pruebas_para_dos_grupos` |
| 20 | Proporciones y variables categóricas | `21_proporciones_y_mas_de_dos_grupos` |
| 25 | Más de dos grupos | `21_proporciones_y_mas_de_dos_grupos` |
| 20 | Tamaño del efecto y ejercicio de la sesión | `22_tamano_del_efecto` |

### Sesión 7 · Módulo IV: Proyecto integrador

**Notebooks:** [`23_eda_completo_con_mpg`](23_eda_completo_con_mpg.ipynb), [`24_reproducibilidad_y_arranque_del_proyecto`](24_reproducibilidad_y_arranque_del_proyecto.ipynb).

**Descripción:** En esta sesión se recorrerá de principio a fin un flujo de EDA reproducible sobre `mpg`: pregunta, auditoría de calidad, limpieza, distribuciones, relaciones, una prueba con tamaño del efecto y conclusiones. Después, cada participante arrancará su proyecto con la plantilla `proyecto/plantilla_proyecto_integrador.ipynb`.

**Objetivo:** **Recorrer un EDA completo y reproducible sobre un *dataset* nuevo, tomando y documentando cada decisión.**

Al terminar, el participante podrá:
1. Seguir la estructura pregunta → datos → calidad → descripción → relaciones → inferencia → conclusiones.
2. Escribir funciones reutilizables para auditar y resumir cualquier *dataset*.
3. Detectar un confusor en un análisis real y ajustar la conclusión.
4. Arrancar tu proyecto: preguntas y auditoría inicial.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Estructura de un EDA | `23_eda_completo_con_mpg` |
| 60 | Demostración en vivo con `mpg` | `23_eda_completo_con_mpg` |
| 15 | Buenas prácticas de reproducibilidad | `24_reproducibilidad_y_arranque_del_proyecto` |
| 35 | Taller: arranque del proyecto | `24_reproducibilidad_y_arranque_del_proyecto` |

### Sesión 8 · Módulo IV: Proyecto integrador

**Notebooks:** [`25_estructura_del_informe_y_comunicacion`](25_estructura_del_informe_y_comunicacion.ipynb), [`26_del_notebook_al_informe`](26_del_notebook_al_informe.ipynb).

**Descripción:** En esta sesión se convertirá el análisis en un informe claro, honesto sobre sus límites y orientado a la decisión: estructura del informe, cómo comunicar intervalos de confianza y tamaños del efecto en lenguaje llano, la gráfica final, la exportación con `nbconvert` y la revisión entre pares. Al final se presenta la **Evaluación semanal 2** y se cierra el curso.

**Objetivo:** **Convertir un análisis exploratorio en un informe de hallazgos claro, verificable y sin afirmaciones que los datos no respaldan.**

Al terminar, el participante podrá:
1. Estructurar un informe: resumen ejecutivo, datos y método, hallazgos, limitaciones y recomendaciones.
2. Traducir un IC y un tamaño del efecto a frases en lenguaje llano, sin exagerar ni usar lenguaje causal injustificado.
3. Diseñar la gráfica final de un hallazgo.
4. Exportar un *notebook* a HTML (y a PDF) con `nbconvert`, con o sin el código.
5. Revisar el informe de un compañero con una lista de verificación.

**Agenda (120 min):**

| Min | Bloque | Notebook |
|---|---|---|
| 10 | Repaso | `25_estructura_del_informe_y_comunicacion` |
| 25 | Estructura del informe | `25_estructura_del_informe_y_comunicacion` |
| 20 | Comunicar números: IC y tamaño del efecto en lenguaje llano, gráfica final, qué no afirmar | `25_estructura_del_informe_y_comunicacion` |
| 15 | Del *notebook* al informe: exportación con `nbconvert` | `26_del_notebook_al_informe` |
| 30 | Taller de redacción del proyecto y revisión entre pares | `26_del_notebook_al_informe` |
| 20 | Presentaciones relámpago, Evaluación semanal 2 y cierre del curso | `26_del_notebook_al_informe` |

## Resultados de aprendizaje por módulo

- I. Datos y su calidad: clasificar variables, auditar calidad y tratar faltantes de forma justificada.
- II. Describir y comparar: describir distribuciones con medidas robustas, detectar atípicos, comparar grupos y comunicar relaciones sin confundir correlación con causalidad.
- III. Inferencia estadística: cuantificar la incertidumbre (IC, *bootstrap*) y aplicar pruebas con supuestos revisados y tamaño del efecto.
- IV. Proyecto integrador: ejecutar un EDA reproducible y redactar un informe de hallazgos honesto sobre sus límites.

## Evaluación

- **Evaluación semanal 1 (E1, Módulos I y II):** 100 pts = cuestionario 40 (Google Forms, 10 preguntas de 4 pts, un intento) + notebook 60 (`evaluaciones/eval1_eda_descriptivo.ipynb` con `tips`). Se publica al terminar la Sesión 4 y cierra al final de la semana 1.
- **Evaluación semanal 2 (E2, Módulos III y IV):** 100 pts = cuestionario 30 (10 preguntas de 3 pts, un intento) + Proyecto integrador 70. Se publica al terminar la Sesión 8 y cierra al final de la semana 2. La consigna del proyecto se publica en la Sesión 5 (`18_bootstrap_e_interpretacion_de_intervalos.ipynb`).
- **Calificación final = (E1 + E2) / 2.** En Classroom: categorías "Evaluación semanal 1" (50%) y "Evaluación semanal 2" (50%).
- **Diploma:** calificación final ≥ 70 **y** asistencia a al menos 7 de 8 sesiones (80%; máximo una falta).
- Las fechas y horas exactas de publicación y cierre de cada evaluación se anuncian en Classroom.

### Reglas abiertas

- **Por definir:** si además se exige un mínimo de 70 en cada evaluación por separado. Fijarlo antes de la Sesión 1 y publicarlo en el tema de bienvenida.
- **Sugerido:** entregas tardías hasta 48 h con 10% de penalización; después no se califican.
- **Sugerido:** cuenta como asistencia estar conectado al menos 90 de los 120 minutos; ver la grabación no cuenta.
- **Sugerido:** un dataset propio para el proyecto debe aprobarse a más tardar en la Sesión 6.

## Rúbrica del notebook de E1 (60 puntos)

- 10 pts: Calidad y tipos de variables (auditoría de duplicados, faltantes y `dtypes`).
- 12 pts: Descripción y valores atípicos.
- 12 pts: Agregación y comparación por `day`, `time` y `smoker`.
- 12 pts: Visualizaciones (tipo adecuado, ejes y unidades rotulados).
- 8 pts: Conclusiones respaldadas y sin lenguaje causal.
- 6 pts: Reproducibilidad (corre de principio a fin).

## Rúbrica del Proyecto integrador (70 puntos, parte de E2)

- 6 pts: Preguntas y contexto.
- 10 pts: Calidad de datos (auditoría y decisiones justificadas).
- 12 pts: Descripción y visualización.
- 16 pts: Inferencia (pruebas adecuadas, supuestos, IC o *bootstrap*, tamaño del efecto).
- 16 pts: Informe de hallazgos (resumen ejecutivo, incertidumbre, limitaciones).
- 10 pts: Reproducibilidad en Codespaces.

Escala por criterio: Excelente = 100%, Suficiente ≈ 60%, Insuficiente = 0-30%. Detalle completo en el mapa de sesiones.

## Checklist previa a clase

- Codespace creado desde `main` y dependencias instaladas (`postCreateCommand`).
- Los *notebooks* de la sesión y sus versiones en `soluciones/` corren de principio a fin (workflow `notebooks-smoke.yml` en verde).
- Datos disponibles en `data/` (no se necesita internet).
- Material de la sesión publicado en el tema correspondiente de Classroom.
- Formulario de pase de lista abierto durante los primeros 30 minutos y al cierre.

## Checklist de cierre de sesión

- Se cubrieron los objetivos de la sesión.
- Asistencia registrada en la hoja (P / F / R) con el reporte de Meet y el formulario.
- Grabación y práctica sin calificación publicadas en Classroom.
- Aviso privado a quien acumule su primera falta; contactar antes de la sesión 3 a quien falte a las sesiones 1 y 2.
- Dudas frecuentes registradas para mejorar los notebooks.

## Riesgos comunes y mitigación

- Diferencias de entorno: usar Codespaces por defecto (Python 3.12 y versiones mínimas `>=` en `requirements.txt`, con *pandas* 3).
- Codespace lento la primera vez: pedir a los alumnos que lo creen antes de la sesión 1.
- Tiempo insuficiente: priorizar ejercicios 🟢 y dejar los retos 🔴 como práctica.
- `penguins_limpio.csv` desalineado: `09_auditoria_de_calidad.ipynb` lo regenera y los *notebooks* `10` en adelante lo recrean si no existe; la versión del repositorio es la de referencia.
