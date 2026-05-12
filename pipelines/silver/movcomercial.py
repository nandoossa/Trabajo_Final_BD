from pyspark import pipelines as dp

@dp.materialized_view(
    comment="Carga de datos desde tabla existente - Capa Bronze"
)
def bronze_movcomercial():
    """
    Lee los datos desde la tabla workspace.bronze.movcomercial
    """
    return spark.read.table("workspace.bronze.movcomercial")
