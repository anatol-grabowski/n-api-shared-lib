BUILD_DIR=./build

build-lib:
	mkdir -p $(BUILD_DIR)
	gcc -fPIC mylib.c -c -o $(BUILD_DIR)/mylib-dynamic.o
	gcc $(BUILD_DIR)/mylib-dynamic.o -shared -o $(BUILD_DIR)/libmylib.so

build-main-with-lib: build-lib
	gcc -c main.cpp -o $(BUILD_DIR)/main.o
	cd $(BUILD_DIR) && gcc main.o -o main -L. -lmylib

run-main-with-lib:
	export LD_LIBRARY_PATH="$$(pwd)/build:$$LD_LIBRARY_PATH" && build/main

build-main:
	mkdir -p $(BUILD_DIR)
	gcc mylib.c -c -o $(BUILD_DIR)/mylib.o
	gcc main.c -c -o $(BUILD_DIR)/main.o
	gcc $(BUILD_DIR)/mylib.o $(BUILD_DIR)/main.o -o $(BUILD_DIR)/a.out

clean:
	rm -rf $(BUILD_DIR)

.PHONY: build-lib build-main clean
