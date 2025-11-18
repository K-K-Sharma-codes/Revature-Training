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
numbers = [1, 2, 3, 4, 5]
rdd = sc.parallelize(numbers)
print("Original RDD: ", rdd.collect())
print(rdd.first())

#
# #transformations
# doubled = rdd.map(lambda x: x * 2)
# print(type(doubled))
# print("Doubled:", doubled.collect())
#
# evens = rdd.filter(lambda x: x%2 == 0)
# print(type(evens))
# print("Even Numbers", evens.collect())
#
# total = rdd.reduce(lambda a, b: a + b)
# print(type(total))
# print("Sum:", total)



# dfstud = spark.read.csv("../data/student.csv", header=True, inferSchema=True, sep=',')
# dfstud.createOrReplaceTempView("students")
# dfstud.show()

# df = spark.read.csv("../data/student.csv", header=True, inferSchema=True, sep=',')
# df.createOrReplaceTempView("students")
# df.printSchema()
#
# high_mark1 = spark.sql("SELECT name, mark1 from students WHERE mark > 10")
# high_mark1.show()
#
# mark2_avg = spark.sql("SELECT dept, avg(mark) as avg from students by dept order by avg")
# mark2_avg.show()

# data = [("a", 10), ("b", 2), ("a", 5), ("b", 20)]
# data = [(1,'a'), (2,'b'), (2,'c')]
# pairRdd = sc.parallelize(data)
# print('Original :' , pairRdd.collect())
#
# sumByKey = pairRdd.reduceByKey(lambda x, y: x + y)
# print('Reduced :', sumByKey.collect())

# rdd = sc.textFile("../data/emp.txt")
# print(rdd.take(5))
#
# rdd.saveAsTextFile("../data/sample_output.txt")

# emprdd = sc.textFile("../data/student.csv")
# print(emprdd.take(5))

# acc = sc.accumulator(0)
# rdd = sc.parallelize([1, 2, 3, 4, 5])
# rdd.foreach(lambda x: acc.add(x))
# print("Accumulator Sum:", acc.value)
#
# b_var = sc.broadcast(["a", "the", "is"])
# print("Broadcast Value:", b_var.value)

# stopwords = ["is", "a", "the", "and", "of"]
# b_stop = sc.broadcast(stopwords)
#
# rdd = sc.textFile("../data/article.txt")
# words = rdd.flatMap(lambda x: x.lower().split())
# filtered = words.filter(lambda w: w not in b_stop.value)
# pairs = filtered.map(lambda w: (w, 1))
# wordCount = pairs.reduceByKey(lambda a, b: a + b)
# print(wordCount.collect())
# wordCount.saveAsTextFile("../output/wordcount")