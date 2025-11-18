from pyspark

# Create a spark session
spark = SparkSession.builder \
    .appName("Local PySpark") \
    .getOrCreate()

# Get SparkContext
sc = spark.sparkContext

number = [1, 2, 3, 4, 5]
rdd = sc.parallelize(number)
print("Original RDD:", rdd.collect())