import ctypes
import csv

my_dll = ctypes.WinDLL("../VS2019/src/Debug/BlackScholes.dll")

def ReadCsv(filename):
	close_data = []
	with open(filename, "r") as file_data:
		reader = csv.DictReader(file_data,delimiter=';')
		for line in reader:
			close_data.append(float(line["<CLOSE>"]))
	return close_data


price_data = ReadCsv("../data/SPFB.BR-4.20_200101_200311.csv")
float_array_type = ctypes.c_double * len(price_data)
my_dll.BlackScholes_Foo(float_array_type(*price_data), len(price_data))
