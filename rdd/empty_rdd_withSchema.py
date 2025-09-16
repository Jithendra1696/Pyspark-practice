
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType
spark = SparkSession.builder.appName("creating empty rdd with schema").getOrCreate()
empty_rdd = spark.sparkContext.emptyRDD()
schema = StructType([
    StructField("First name",StringType(),True),
    StructField("Last name",StringType(),True),
    StructField("City",StringType(),True)
])

df = spark.createDataFrame(empty_rdd,schema)
df.printSchema()
