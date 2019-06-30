import ctypes

lib = ctypes.cdll.LoadLibrary('./build/libmylib.so')
lib.print()
