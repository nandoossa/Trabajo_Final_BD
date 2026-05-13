# Arquitectura ELT en Databricks para análisis comercial y abastecimiento de inventario  
## Metodología Medallion

![Databricks](https://img.shields.io/badge/Databricks-ELT-red?logo=databricks)
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-Big%20Data-orange?logo=apachespark)
![Python](https://img.shields.io/badge/Python-Data%20Engineering-blue?logo=python)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Medallion-green)

---

# 📌 Descripción del Proyecto

Este proyecto implementa una arquitectura **ELT en Databricks** utilizando la metodología **Medallion (Bronze, Silver y Gold)** para el análisis comercial y la optimización del abastecimiento de inventario.

El pipeline procesa información histórica de:

- Ventas
- Devoluciones
- Productos
- Movimientos comerciales

El objetivo principal es transformar datos crudos en información confiable y generar un **modelo de sugerido de compras** basado en la demanda neta histórica.

---

# 🏗️ Arquitectura Medallion

```text
Fuente CSV
   ↓
Bronze → Datos crudos
   ↓
Silver → Limpieza y transformación
   ↓
Gold → KPIs y modelo analítico
```

---

# ⚙️ Tecnologías Utilizadas

- Databricks
- Apache Spark
- PySpark
- Delta Lake
- Python
- Matplotlib
- Unity Catalog
- Databricks Workflows

---

# 📂 Estructura del Proyecto

```text
Trabajo_Final_BD/
│
├── 01_ingestar_datos_bronze.ipynb
├── 02_silver.ipynb
├── 03_gold.ipynb
├── 04_modelo_compras.ipynb
│
├── images/
│   ├── arquitectura_medallion.png
│   ├── pipeline.png
│   ├── job_ingesta.png
│   ├── top20_ventas.png
│   └── sugerido_compras.png
│
└── README.md
```

---

# 🥉 Capa Bronze — Ingesta de Datos

La capa Bronze almacena los datos crudos sin modificaciones para mantener la trazabilidad histórica.

## Funciones principales

- Creación de esquemas Bronze/Silver/Gold
- Lectura de archivos CSV
- Conversión de codificación a UTF-8
- Definición de columnas como `string`
- Almacenamiento en formato Delta

## Tabla generada

```sql
workspace.bronze.movcomercial
```

---

# 🥈 Capa Silver — Limpieza y Transformación

En esta etapa se realiza la depuración y normalización de datos.

## Procesos aplicados

- Eliminación de caracteres especiales
- Reemplazo de valores vacíos por NULL
- Eliminación de espacios
- Conversión de tipos numéricos
- Conversión de fechas
- Normalización de texto

## Tabla generada

```sql
workspace.silver.movcomercial
```

---

# 🥇 Capa Gold — Análisis Comercial

La capa Gold genera información analítica lista para consumo.

## Métricas generadas

- Total ventas
- Unidades vendidas
- Rentabilidad
- Ventas por producto
- Devoluciones
- Top productos

---

# 📊 Modelo de Sugerido de Compras

El notebook `04_modelo_compras.ipynb` implementa el modelo final de abastecimiento.

## Fórmula aplicada

```text
(Ventas - Devoluciones) × 1.20
```

## Variables calculadas

| Variable | Descripción |
|---|---|
| VENTAS_NETAS_UNIDADES | Demanda real |
| STOCK_SEGURIDAD | 20% adicional |
| SUGERIDO_COMPRA | Compra recomendada |

---

# 🔄 Orquestación y Automatización

El pipeline fue automatizado usando:

- Databricks Workflows
- Delta Live Tables

---

# 🚀 Cómo Ejecutar el Proyecto

## 1. Clonar repositorio

```bash
git clone https://github.com/nandoossa/Trabajo_Final_BD.git
```

## 2. Importar notebooks en Databricks

- 01_ingestar_datos_bronze.ipynb
- 02_silver.ipynb
- 03_gold.ipynb
- 04_modelo_compras.ipynb

---

# 📚 Repositorio GitHub

🔗 https://github.com/nandoossa/Trabajo_Final_BD

---

# 👨‍💻 Autores

## Raúl Fernando Ossa Ramírez
Universidad Autónoma Latinoamericana (UNAULA)

## Jennifer Alejandra López Sánchez
Universidad Autónoma Latinoamericana (UNAULA)

---

# 🎓 Información Académica

**Asignatura:** Big Data  
**Institución:** Universidad Autónoma Latinoamericana — UNAULA  
**Ciudad:** Medellín, Colombia  
**Año:** 2026
