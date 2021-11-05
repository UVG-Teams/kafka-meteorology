# Universidad del Valle de Guatemala
# Redes
# Laboratorio 10
# Jennifer Sandoval	18962
# Francisco Rosal	18676

import time
import json
import sensor
import logging
from kafka import KafkaProducer

SLEEP_TIME = 5
logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s \n', level = logging.INFO)


logging.info('Starting producer')
producer = KafkaProducer(bootstrap_servers='20.120.14.159:9092', value_serializer=lambda value: json.dumps(value).encode('utf-8'))

while True:
    current_log = sensor.log()
    logging.info('Sending message: {}'.format(current_log))

    producer.send('meteorology-18676', value=current_log)

    time.sleep(SLEEP_TIME)
