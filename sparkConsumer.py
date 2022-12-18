from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from elasticsearch import Elasticsearch

spark = SparkSession.builder.appName("Kafka-Elasticsearch Consumer").getOrCreate()
sc = spark.sparkContext
ssc = StreamingContext(sc, 1) 

kafka_stream = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'fuelPrice': 1})

es = Elasticsearch(["http://localhost:9200"])

def send_to_elasticsearch(rdd):
    # Convert RDD to JSON
    data_json = rdd.map(lambda x: x[1]).collect()
    # Send data to Elasticsearch
    for record in data_json:
        es.index(index='fuelprice', body=record)

kafka_stream.foreachRDD(send_to_elasticsearch)
ssc.start()
ssc.awaitTermination()