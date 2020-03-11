import ctypes
import csv
import matplotlib.pyplot as plt
import numpy as np

my_dll = ctypes.WinDLL("../VS2019/src/Debug/BlackScholes.dll")

def ReadCsv(filename):
	close_data = []
	with open(filename, "r") as file_data:
		reader = csv.DictReader(file_data,delimiter=';')
		for line in reader:
			close_data.append(float(line["<CLOSE>"]))
	return close_data


price_data = ReadCsv("../data/SPFB.BR-4.20_200101_200311.csv")
#float_array_type = ctypes.c_double * len(price_data)
#my_dll.BlackScholes_Foo(float_array_type(*price_data), len(price_data))

fig = plt.figure()
#ax = plt.axes(projection='3d')
x = np.arange(0, len(price_data))

plt.plot(x, price_data, label='BR-4.20 price')
plt.legend()

plt.show()
