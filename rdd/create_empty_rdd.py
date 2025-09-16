# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName("empty rdd creation").getOrCreate()
# empty_rdd = spark.sparkContext.emptyRDD()
# print(empty_rdd)

# ------------------------

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("empty-rdd-creation-using-parallize").getOrCreate()
rdd = spark.sparkContext.parallelize([])
print(rdd)