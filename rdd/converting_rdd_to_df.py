from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType
spark = SparkSession.builder.appName("converting rdd to df").getOrCreate()
empty_rdd = spark.sparkContext.emptyRDD()
schema =StructType([
    StructField("First Name",StringType(),True),
    StructField("Last Name",StringType(),True),
    StructField("City",StringType(),True)
])
df = empty_rdd.toDF(schema)
df.show()