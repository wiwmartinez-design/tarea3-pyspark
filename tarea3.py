"""
=============================================================================
UNAD - Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)
Curso: Big Data - Tarea 3: Procesamiento de Datos con Apache Spark
Autor: William Jesús Insandará Martínez
Descripción: Pipeline de procesamiento por lotes (Batch Processing) para el
             Análisis Exploratorio de Datos (EDA) de la serie histórica TRM.
=============================================================================
"""

from pyspark.sql import SparkSession

def main():
    # 1. Inicialización de la sesión distribuida de Apache Spark
    spark = SparkSession.builder \
        .appName("Tarea3_Procesamiento_Batch_TRM") \
        .getOrCreate()

    # Reducción de logs en consola para visualizar resultados limpiamente
    spark.sparkContext.setLogLevel("ERROR")

    # 2. Carga del conjunto de datos e inferencia automática del esquema
    # Dataset: Serie Histórica de la TRM en Colombia (8.358 registros)
    df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv("rows.csv")

    # 3. Validación estructural y visualización de muestra inicial
    print("\n--- Estructura del Esquema Relacional ---")
    df.printSchema()

    print("\n--- Primeros 5 Registros del Conjunto de Datos ---")
    df.show(5)

    # 4. Análisis Exploratorio de Datos (EDA): Estadísticas Descriptivas
    print("\n--- Resumen Estadístico Descriptivo (Batch EDA) ---")
    df.describe().show()

    # 5. Cierre ordenado del contexto distribuido y liberación de memoria
    spark.stop()

if __name__ == "__main__":
    main()
