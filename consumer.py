# Universidad del Valle de Guatemala
# Redes
# Laboratorio 10
# Jennifer Sandoval	18962
# Francisco Rosal	18676

import logging
from kafka import KafkaConsumer

# logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s \n', level = logging.INFO)
logging.basicConfig(format='%(message)s \n', level = logging.INFO)


logging.info('Starting consumer')
consumer = KafkaConsumer('meteorology-18676', bootstrap_servers=['20.120.14.159:9092'])

def special_decode(payload):
    wind_options = ['N','NW','W','SW','S','SE','E','NE']

    log = payload.decode('ASCII')
    data = []
    for i in log:
        data.append(i)

    temperature = ord(data[0])
    humidity = ord(data[1])
    wind = wind_options[ord(data[2]) - 100]

    return temperature, humidity, wind


for msg in consumer:
    logging.info('Received message: {}'.format(msg.value))
    logging.info("Payload size is {} bytes".format(len(msg.value)))

    current_log = special_decode(msg.value)
    logging.info('LOG: {}'.format(current_log))
