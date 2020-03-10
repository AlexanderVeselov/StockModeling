import ctypes

my_dll = ctypes.WinDLL("../VS2019/src/Debug/BlackScholes.dll")
my_dll.BlackScholes_Foo()
