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

# Step 2: Create an RDD from a python list
from pyspark.sql.types import StringType, IntegerType, StructType, StructField


schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])

data = [("Alice", 25), ("Bob", 30)]
df = spark.createDataFrame(data, schema)
print('Schema')
df.printSchema()
print('Dataframe')
df.show()

