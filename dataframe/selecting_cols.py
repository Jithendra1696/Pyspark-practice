from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName("selecting cols").getOrCreate()

data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]
columns = ["firstname","lastname","country","state"]

df = spark.createDataFrame(data=data,schema=columns)
# df.show()

df.select("firstname","lastname").show()
df.select(df["country"]).show()
df.select(col("state")).show()

# selecting all cols
df.select([cols for cols in df.columns]).show()