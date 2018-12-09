from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]","deneme")
ssc = StreamingContext(sc, 10)
socket_stream = ssc.socketTextStream("localhost",8888)

random_integers = socket_stream.window( 30 )

digits = random_integers.flatMap(lambda line: line.split(" ")).map(lambda digit: (digit, 1))

digit_count = digits.reduceByKey(lambda x,y:x+y)
digit_count.pprint()

ssc.start()

