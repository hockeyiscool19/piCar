# Define compiler
CC=g++

# Define flags
CFLAGS=-I/usr/local/include/opencv4 `pkg-config --cflags opencv4`
LIBS=`pkg-config --cflags --libs opencv4`

# Define the target executable
TARGET=opencv

# 'all' target
all: $(TARGET)

# Compiling the target
$(TARGET): opencv.cpp
	$(CC) $(CFLAGS) opencv.cpp -o $(TARGET) $(LIBS)

# 'clean' target for cleaning up
clean:
	rm -f $(TARGET)

