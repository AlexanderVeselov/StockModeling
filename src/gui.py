import ctypes
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random
import indicators

class StockLibDll:
	def __init__(self, path):
		self.dll = ctypes.WinDLL(path)

	def CalculateEMA():
		self.dll(float_array_type(*price_data), len(price_data))

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

num_columns = 1
random.seed(0)
stock_lib = ctypes.WinDLL("../VS2019/src/Debug/StockLib.dll")
stock_lib.Ping()

#price_data = ReadCsv("../data/SPFB.BR-4.20_200101_200311.csv")
#float_array_type = ctypes.c_double * len(price_data)
#my_dll.BlackScholes_Foo(float_array_type(*price_data), len(price_data))

fig = plt.figure()
#ax = plt.axes(projection='3d')
price_len = 1000 # len(price_data)
x = np.arange(0, price_len)

ax = fig.add_subplot(2, num_columns, 1)

price_data = GenerateStockPrices(len(x), 1.0)
ax.plot(x, price_data)
price_ema = indicators.SMA(price_data, 3)
ax.plot(x, price_ema)

ax = fig.add_subplot(2, num_columns, 2)
stochastic_data = indicators.StochasticOscillator(price_data, 20)
ax.plot(x, stochastic_data)
stochastic_data_smoothed = indicators.EMA(stochastic_data, 0.5)
ax.plot(x, stochastic_data_smoothed)
stochastic_data_smoothed1 = indicators.SMA(stochastic_data, 3)
ax.plot(x, stochastic_data_smoothed1)
ax.grid()
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
