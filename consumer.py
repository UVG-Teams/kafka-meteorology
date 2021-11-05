# Universidad del Valle de Guatemala
# Redes
# Laboratorio 10
# Jennifer Sandoval	18962
# Francisco Rosal	18676

import logging
from kafka import KafkaConsumer
import matplotlib.pyplot as plt

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

    return {
        "t": temperature,
        "h": humidity,
        "w": wind
    }

all_temp = []
all_hume = []
all_wind = [0,0,0,0,0,0,0,0]
directions = ['N','NW','W','SW','S','SE','E','NE']

for msg in consumer:
    logging.info('Received message: {}'.format(msg.value))

    current_log = special_decode(msg.value)
    logging.info('LOG: {}'.format(current_log))
    all_temp.append(current_log ['t'])
    all_hume.append(current_log['h'])
    pos = directions.index(current_log['w'])
    all_wind[pos] = all_wind[pos] + 1
    figure, axis = plt.subplots(1, 3)
    axis[0].plot(all_temp,'r')
    axis[0].set_title('Temperatura')
    axis[0].set_ylabel('°C')
    axis[1].plot(all_hume,'g')
    axis[1].set_title('Humedad relativa')
    axis[1].set_ylabel('%')
    axis[2].bar(directions,all_wind)
    axis[2].set_title('Direccion del viento')
    plt.show()

