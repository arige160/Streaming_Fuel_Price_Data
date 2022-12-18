# Streaming_Fuel_Price_Data

# About the project
![img](https://github.com/arige160/Streaming_Fuel_Price_Data/blob/master/Docs/Number_of_records.jpg)
![img](https://github.com/arige160/Streaming_Fuel_Price_Data/blob/master/Docs/Heatmap.jpg)
![img](https://github.com/arige160/Streaming_Fuel_Price_Data/blob/master/Docs/graph.jpg)
![img](https://github.com/arige160/Streaming_Fuel_Price_Data/blob/master/Docs/graphs.jpg)


This project consists of creating a whole pipeline diffusing streaming fuel prices in the area of france. The project is devolopped with kafka, spark, elasticsearch and kibana for visualization.

# Prerequisites:
The project is was devoloped with the following Prerequisites:
  * Kafka 3.2.0
  * Scala 
  * JDK 8.0
  * Python 3.7.0
  * Spark 2.4.6
  * Elasticsearch 7.17.5
  * Kibana 7.17.5
# Pipeline :

This project is composed of the following main steps:
   ###### Data Processing:
 Data ingestion from a streaming data API and training a machine learning model to predict the fuel price based on its type(Gazoal, ..).
 
  ###### Data indexing to elasticsearch:
 After creating an index within elasticsearch, we wreated a spark consumer in order to read from kafka topic and send data into the index in real time.
 
  ###### Visualization:
  
 In order to visualize the streaming data, we used Kibana dashboard. Creating costumized visualizations:
 
  * Number of records: keep up with uploaded records into elasticsearch.
  * A heatmap        : locate fuel station in france, specifying the fuel name and their prices( indicated with radius of the cercle).
  * The variation of fuel prices based on cities.
            
 # Contribution:
  * Flihi Arij 
  * Sadkaoui Marwa
INDP3_AIM, SUPCOM 2023_2022
