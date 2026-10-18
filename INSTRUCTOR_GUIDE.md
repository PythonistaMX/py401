# Instructor Guide - Py401

Guía operativa para impartir **Py401 · EDA Práctico** con consistencia técnica y pedagógica. Fuente: mapa de sesiones del curso. Horarios en hora de la Ciudad de México (CDMX).

## Estructura (8 sesiones, 2 horas, lun-jue 6:30-8:30 pm)

1. Sesión 1 (lun 19 oct): *NumPy* y *pandas* esenciales, tipos de variables, sesgos de recolección (`01`).
2. Sesión 2 (mar 20 oct): calidad de datos y valores faltantes (`02`; genera `data/penguins_limpio.csv`).
3. Sesión 3 (mié 21 oct): estadística descriptiva, forma de la distribución y valores atípicos (`03`).
4. Sesión 4 (jue 22 oct): agregación, relaciones y visualización efectiva (`04`). Se publica la Evaluación semanal 1.
5. Sesión 5 (lun 26 oct): incertidumbre, intervalos de confianza y *bootstrap* (`05`). Se publica la consigna del Proyecto integrador.
6. Sesión 6 (mar 27 oct): pruebas de hipótesis y tamaño del efecto (`06`).
7. Sesión 7 (mié 28 oct): EDA completo paso a paso con `mpg` y arranque del proyecto (`07`).
8. Sesión 8 (jue 29 oct): informe de hallazgos y presentación (`08`). Se publica la Evaluación semanal 2.

## Resultados de aprendizaje por módulo

- I. Datos y su calidad: clasificar variables, auditar calidad y tratar faltantes de forma justificada.
- II. Describir y comparar: describir distribuciones con medidas robustas, detectar atípicos, comparar grupos y comunicar relaciones sin confundir correlación con causalidad.
- III. Inferencia estadística: cuantificar la incertidumbre (IC, *bootstrap*) y aplicar pruebas con supuestos revisados y tamaño del efecto.
- IV. Proyecto integrador: ejecutar un EDA reproducible y redactar un informe de hallazgos honesto sobre sus límites.

## Evaluación

- **Evaluación semanal 1 (E1, Módulos I y II):** 100 pts = cuestionario 40 (Google Forms, 10 preguntas de 4 pts, un intento) + notebook 60 (`eval1_eda_descriptivo.ipynb` con `tips`). Publica jue 22 oct 8:30 pm, cierra dom 25 oct 11:59 pm.
- **Evaluación semanal 2 (E2, Módulos III y IV):** 100 pts = cuestionario 30 (10 preguntas de 3 pts, un intento) + Proyecto integrador 70. Publica jue 29 oct 8:30 pm, cierra dom 1 nov 11:59 pm. La consigna del proyecto se publica el lun 26 oct.
- **Calificación final = (E1 + E2) / 2.** En Classroom: categorías "Evaluación semanal 1" (50%) y "Evaluación semanal 2" (50%).
- **Diploma:** calificación final ≥ 70 **y** asistencia a al menos 7 de 8 sesiones (80%; máximo una falta).

### Reglas abiertas

- **Por definir:** si además se exige un mínimo de 70 en cada evaluación por separado. Fijarlo antes del 19 oct y publicarlo en el tema de bienvenida.
- **Sugerido:** entregas tardías hasta 48 h con 10% de penalización; después no se califican.
- **Sugerido:** cuenta como asistencia estar conectado al menos 90 de los 120 minutos; ver la grabación no cuenta.
- **Sugerido:** un dataset propio para el proyecto debe aprobarse a más tardar el mar 27 oct.

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
- El notebook de la sesión y su versión en `soluciones/` corren de principio a fin (workflow `notebooks-smoke.yml` en verde).
- Datos disponibles en `data/` (no se necesita internet).
- Material de la sesión publicado en el tema correspondiente de Classroom.
- Formulario de pase de lista abierto de 6:30 a 7:00 pm y al cierre.

## Checklist de cierre de sesión

- Se cubrieron los objetivos de la sesión.
- Asistencia registrada en la hoja (P / F / R) con el reporte de Meet y el formulario.
- Grabación y práctica sin calificación publicadas en Classroom.
- Aviso privado a quien acumule su primera falta; contactar antes de la sesión 3 a quien falte a las sesiones 1 y 2.
- Dudas frecuentes registradas para mejorar los notebooks.

## Riesgos comunes y mitigación

- Diferencias de entorno: usar Codespaces por defecto (Python 3.12, versiones fijas en `requirements.txt`).
- Codespace lento la primera vez: pedir a los alumnos que lo creen antes de la sesión 1.
- Tiempo insuficiente: priorizar ejercicios 🟢 y dejar los retos 🔴 como práctica.
- `penguins_limpio.csv` desalineado: el notebook 02 lo regenera; la versión del repositorio es la de referencia.
