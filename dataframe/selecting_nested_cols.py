from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

spark=SparkSession.builder.appName("creation of custom schema with nested data").getOrCreate()
data =  [
    (("James","","Smith"),"36636","M",3100),
    (("Michael","Rose",""),"40288","M",4300),
    (("Robert","","Williams"),"42114","M",1400),
    (("Maria","Anne","Jones"),"39192","F",5500),
    (("Jen","Mary","Brown"),"","F",-1)
  ]
schema = StructType([
    StructField("name",StructType([
        StructField("First name",StringType(),True),
        StructField("Middle name",StringType(),True),
        StructField("Last name",StringType(),True),
    ])),
    StructField("Id",StringType(),True),
    StructField("Gender",StringType(),True),
    StructField("Salary",StringType(),True),
])
df = spark.createDataFrame(data=data,schema=schema)
df.show()
df.select("name.First name").show()