from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType
spark = SparkSession.builder.appName("custom schema creation").getOrCreate()

data = [("James","","Smith","36636","M",3000),
    ("Michael","Rose","","40288","M",4000),
    ("Robert","","Williams","42114","M",4000),
    ("Maria","Anne","Jones","39192","F",4000),
    ("Jen","Mary","Brown","","F",-1)
  ]
schema = StructType([
    StructField("first name",StringType(),True),
    StructField("middle name",StringType(),True),
    StructField("last name",StringType(),True),
    StructField("id",StringType(),True),
    StructField("gender",StringType(),True),
    StructField("salary",StringType(),True)
])

df = spark.createDataFrame(data=data,schema=schema)
df.show()