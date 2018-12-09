from pyspark import SparkContext
from pyspark.streaming import StreamingContext
ssc = StreamingContext(sc, 1)

# Create a DStream that will connect to hostname:port, like localhost:9999
lines_RDD = ssc.socketTextStream("localhost", 8888)

# Split each line into words
data_RDD = lines_RDD.flatMap(lambda line: line.split(","))

data_RDD.pprint()

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate
