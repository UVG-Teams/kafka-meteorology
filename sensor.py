#Universidad del Valle de Guatemala
#Redes
#Laboratorio 10 
#Jennifer Sandoval	18962
#Francisco Rosal	18676

from pylab import *
import json 

def reading_temperature():
	return round(float(uniform(0, 100.00, 1)),2)

def reading_RH():
	return int(uniform(0,100, 1))

def reading_wind_direction():
	directions = ['N','NW','W','SW','S','SE','E','NE']
	position = int(randint(0,7,size=1))
	#print(position)
	return directions[position]


def to_JSON():
	temperature = reading_temperature()
	relative_humidity = reading_RH()
	direction = reading_wind_direction()
	data = {"temperatura": temperature, "humedad": relative_humidity, "direccion_viento": direction}
	return data
