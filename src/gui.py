import ctypes
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

my_dll = ctypes.WinDLL("../VS2019/src/Debug/BlackScholes.dll")

def ReadCsv(filename):
	close_data = []
	with open(filename, "r") as file_data:
		reader = csv.DictReader(file_data,delimiter=';')
		for line in reader:
			close_data.append(float(line["<CLOSE>"]))
	return close_data

def GenerateStockPrices(size, start_price):
	prices = []
	current_price = start_price
	for t in range(0, size):
		delta_price = current_price * 0.0001 + random.gauss(0, 1) * current_price * 0.02
		current_price += delta_price
		prices.append(current_price)
	return prices

def lerp(a, b, t):
	return a * (1 - t) + b * t

def CalcEMA(input_data, hysteresis):
	output_ema = [input_data[0]]
	for i in range(1, len(input_data)):
		ema = lerp(input_data[i], output_ema[i - 1], hysteresis)
		output_ema.append(ema)
	return output_ema

num_columns = 1

#price_data = ReadCsv("../data/SPFB.BR-4.20_200101_200311.csv")
#float_array_type = ctypes.c_double * len(price_data)
#my_dll.BlackScholes_Foo(float_array_type(*price_data), len(price_data))

fig = plt.figure()
#ax = plt.axes(projection='3d')
x = np.arange(0, 1000)

ax = fig.add_subplot(1, num_columns, 1)

for i in range(0, 3):
	price_data = GenerateStockPrices(len(x), 1.0)
	ax.plot(x, price_data)
	price_ema = CalcEMA(price_data, 0.9)
	ax.plot(x, price_ema)

#ax = fig.add_subplot(1, num_columns, 2, projection='3d')
##ax = fig.add_subplot(111, projection='3d')
#
#X = np.arange(-5, 5, 0.25)
#Y = np.arange(-5, 5, 0.25)
#X, Y = np.meshgrid(X, Y)
#print(X)
#Z = np.exp(-0.5 * X**2) * np.exp(-0.5 * Y**2)
#ax.plot_surface(X, Y, Z)

#plt.legend()

plt.show()
