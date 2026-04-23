# Step 1: Start Hadoop/Spark services
start-all.sh

# Step 2: Go to Spark directory
cd ~/spark-3.5.2-bin-hadoop3

# Step 3: Create input file
nano sparkcount.txt

hello world hello spark
spark is fast

Ctrl + O → Enter
Ctrl + X

./bin/spark-shell

// Load text file into RDD
val rdd = spark.sparkContext.textFile("/home/hadoop/spark-3.5.2-bin-hadoop3/sparkcount.txt")

// Split lines into words
val rdd1 = rdd.flatMap(line => line.split(" "))

// Map each word to (word, 1)
val rdd2 = rdd1.map(x => (x, 1))

// Reduce by key to count occurrences
val rdd3 = rdd2.reduceByKey((a, b) => a + b)

// Display result
rdd3.collect()

// Optional: Convert to DataFrame and show
rdd3.toDF("word", "count").show()
