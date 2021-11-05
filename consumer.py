# Universidad del Valle de Guatemala
# Redes
# Laboratorio 10
# Jennifer Sandoval	18962
# Francisco Rosal	18676

import json
import logging
from kafka import KafkaConsumer

logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s \n', level = logging.INFO)


logging.info('Starting consumer')
consumer = KafkaConsumer('meteorology-18676', bootstrap_servers=['20.120.14.159:9092'])

for msg in consumer:
    current_log = json.loads(msg.value)
    logging.info('Received message: {}'.format(current_log))
