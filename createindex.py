from elasticsearch import Elasticsearch

# Connect to the Elasticsearch cluster
es = Elasticsearch(["http://localhost:9200"])

# Define the index pattern and mapping
index_pattern = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
    "properties": {
      "datasetid": {
        "type": "keyword"
      },
      "recordid": {
        "type": "keyword"
      },
      "fields": {
        "type": "object",
        "properties": {
          "ville": {
            "type": "keyword"
          },
          "pop": {
            "type": "keyword"
          },
          "reg_name": {
            "type": "keyword"
          },
          "com_arm_code": {
            "type": "keyword"
          },
          "dep_name": {
            "type": "keyword"
          },
          "prix_nom": {
            "type": "keyword"
          },
          "com_code": {
            "type": "keyword"
          },
          "epci_name": {
            "type": "keyword"
          },
          "dep_code": {
            "type": "keyword"
          },
          "services_service": {
            "type": "keyword"
          },
          "prix_id": {
            "type": "keyword"
          },
          "horaires_automate_24_24": {
            "type": "keyword"
          },
          "horaires": {
            "type": "text"
          },
          "com_arm_name": {
            "type": "keyword"
          },
          "prix_maj": {
            "type": "date"
          },
          "id": {
            "type": "keyword"
          },
          "reg_code": {
            "type": "keyword"
          },
          "adresse": {
            "type": "text"
          },
          "epci_code": {
            "type": "keyword"
          },
          "cp": {
            "type": "keyword"
          },
          "prix_valeur": {
            "type": "float"
          },
          "com_name": {
            "type": "keyword"
          }
        }
      },
      "geometry": {
        "type": "geo_shape"
      }
    }
  }
}

# Create the index
es.indices.create(index="fuelprice", body=index_pattern)
