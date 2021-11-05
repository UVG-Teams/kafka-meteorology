# Universidad del Valle de Guatemala
# Redes
# Laboratorio 10
# Jennifer Sandoval	18962
# Francisco Rosal	18676

import time
import sensor
import logging
from kafka import KafkaProducer

SLEEP_TIME = 5
# logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s \n', level = logging.INFO)
logging.basicConfig(format='%(message)s \n', level = logging.INFO)


logging.info('Starting producer')
producer = KafkaProducer(bootstrap_servers = '20.120.14.159:9092')

def special_encode(log):
    wind_options = ['N','NW','W','SW','S','SE','E','NE']

    temperature = int(log['t'])
    humidity = log['h']
    wind = wind_options.index(log['w']) + 100

    data = "{}{}{}".format(chr(temperature), chr(humidity), chr(wind))
    return data.encode('ASCII')


while True:
    current_log = sensor.log()
    logging.info('Sending message: {}'.format(current_log))

    payload = special_encode(current_log)

    producer.send('meteorology-18676', value=payload)
    time.sleep(SLEEP_TIME)
