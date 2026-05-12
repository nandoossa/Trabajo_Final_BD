from pyspark import pipelines as dp
from pyspark.sql.functions import (
    col, upper, trim, abs, first, regexp_replace, 
    expr, round, countDistinct, sum, avg
)

@dp.materialized_view(
    comment="Análisis de ventas por producto - Capa Gold"
)
def ventas_producto():
    """
    Agregación de métricas de ventas por producto:
    - Total de facturas de venta
    - Unidades vendidas
    - Ingresos totales (con y sin IVA)
    - Rentabilidad promedio por producto
    
    Filtra solo documentos de tipo FV00 (Facturas de Venta)
    """
    # Leer datos desde Silver
    df = spark.read.table("movcomercial")
    
    # Normalizar CLASE
    df = df.withColumn(
        "CLASE",
        upper(trim(col("CLASE")))
    )
    
    # Limpiar y convertir CANTIDAD
    df = df.withColumn(
        "CANTIDAD_TMP",
        regexp_replace(col("CANTIDAD"), r"\.", "")
    )
    df = df.withColumn(
        "CANTIDAD_TMP",
        regexp_replace(col("CANTIDAD_TMP"), ",", ".")
    )
    df = df.withColumn(
        "CANTIDAD_TMP",
        expr("try_cast(CANTIDAD_TMP as double)")
    )
    
    # Filtrar solo ventas (FV00)
    df_ventas = df.filter(col("CLASE") == "FV00")
    
    # Agregación por producto
    ventas_producto = df_ventas.groupBy("PRODUCTO").agg(
        first("PRODUCTONO").alias("NOMBRE_PRODUCTO"),
        countDistinct("NUMERO").alias("TOTAL_VENTAS"),
        round(abs(sum("CANTIDAD_TMP")), 2).alias("UNIDADES_VENDIDAS"),
        round(sum("PARCIAL"), 2).alias("PRECIO_VENTA"),
        round(sum("PARCIALANT"), 2).alias("PRECIO_ANTES_IVA"),
        round(avg("RENTABILIDAD") * 100, 2).alias("RENTABILIDAD_PORCENTAJE")
    ).orderBy(col("TOTAL_VENTAS").desc())
    
    return ventas_producto
