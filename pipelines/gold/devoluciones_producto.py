from pyspark import pipelines as dp
from pyspark.sql.functions import (
    col, upper, trim, abs, first, regexp_replace, 
    expr, round, countDistinct, sum, avg
)

@dp.materialized_view(
    comment="Análisis de devoluciones por producto - Capa Gold"
)
def devoluciones_producto():
    """
    Agregación de métricas de devoluciones por producto:
    - Total de documentos de devolución
    - Unidades devueltas
    - Valor total devuelto (con y sin IVA)
    - Rentabilidad promedio por producto
    
    Filtra solo documentos de tipo DV00 (Devoluciones)
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
    
    # Filtrar solo devoluciones (DV00)
    df_devoluciones = df.filter(col("CLASE") == "DV00")
    
    # Agregación por producto
    devoluciones_producto = df_devoluciones.groupBy("PRODUCTO").agg(
        first("PRODUCTONO").alias("NOMBRE_PRODUCTO"),
        countDistinct("NUMERO").alias("TOTAL_DEVOLUCIONES"),
        round(abs(sum("CANTIDAD_TMP")), 2).alias("UNIDADES_DEVUELTAS"),
        round(abs(sum("PARCIAL")), 2).alias("PRECIO_VENTA"),
        round(abs(sum("PARCIALANT")), 2).alias("PRECIO_ANTES_IVA"),
        round(avg("RENTABILIDAD") * 100, 2).alias("RENTABILIDAD_PORCENTAJE")
    ).orderBy(col("TOTAL_DEVOLUCIONES").desc())
    
    return devoluciones_producto
