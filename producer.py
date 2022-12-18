
import urllib.request
import os
import time
from kafka import KafkaProducer
import json
from time import sleep 


# -------------------

bootstrap_servers=['localhost:9092']
producer= KafkaProducer(bootstrap_servers= bootstrap_servers)

url='https://data.economie.gouv.fr/api/records/1.0/search/?dataset=prix-carburants-fichier-instantane-test-ods-copie&q=&facet=id&facet=adresse&facet=ville&facet=prix_maj&facet=prix_nom&facet=com_arm_name&facet=epci_name&facet=dep_name&facet=reg_name&facet=services_service&facet=horaires_automate_24_24'
producer = KafkaProducer(bootstrap_servers =['localhost:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    response= urllib.request.urlopen(url)
    data=json.loads(response.read().decode())
    records=data['records']
    
    for record in records:
        producer.send('fuelPrice', record)
        print(record)
        sleep(2)
        
# -----------------------------------