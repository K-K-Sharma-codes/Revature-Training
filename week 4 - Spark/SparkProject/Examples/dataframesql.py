import sys
import os

# standard line
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-20"
os.environ["SPARK_HOME"] = "D:\Revature Training\week 4 - Spark\SparkProject\.venv\Lib\site-packages\pyspark"   #"D:/Revature Training/week 4 - Spark/SparkProject/.venv/Lib/site-packages/pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Local Pyspark") \
    .getOrCreate()

# Get SparkContext
sc = spark.sparkContext

# data = [("Alice", 25), ("Bob", 30)]
# df = spark.createDataFrame(data,["Name", "Age"])
#
# df.show()
#
# df.select("Name").show()
# df.filter(df.Age > 25).show()
# df.groupby("Age").count().show()
# df.orderBy(df.Age.desc()).show()
#
# from pyspark.sql.functions import col, upper
# df.select(upper(col("Name")).alias("NAME_UPPER")).show()

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# myschema = StructType([
#     StructField("name", StringType(), True),
#     StructField("age", IntegerType(), True),
#     # StructField("_corrupt_record", StringType(), True),
# ])
# df = spark.read.json("../data/file1.json", schema=myschema)
# df.cache()
# df_cleaned = df.filter("name is NOT NULL AND age is NOT NULL")
#
# df_cleaned.show()
# df.printSchema()
#
# df_cleaned.createOrReplaceTempView("people")
# spark.sql("SELECT name from people where age > 28").show()

# df.write.json("../data/output_json")

data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["name", "age"]
df = spark.createDataFrame(data, columns)
df.show()

# df.write.mode("overwrite").parquet("../data/file2.parquet")
# df = spark.read.parquet("../data/file2.parquet")
# df.show()