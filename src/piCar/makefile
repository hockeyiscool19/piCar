# # ariables
# HOST=pi@10.0.0.81
# TARGET_DIR=/home/pi/Desktop/piCar
# EXECUTABLE=main

# # Default target to compile and build the executable
# all:
# 	g++ -Wall -g main.cpp -o $(EXECUTABLE)

# # Target to clean up the generated files
# clean:
# 	rm -f $(EXECUTABLE) $(EXECUTABLE).o

# # Target to run the program locally
# run:
# 	./$(EXECUTABLE)

# # Target to transfer and run on Raspberry Pi
# deploy: all
# 	scp $(EXECUTABLE) $(HOST):$(TARGET_DIR)
# 	ssh $(HOST) 'cd $(TARGET_DIR); chmod +x $(EXECUTABLE); ./$(EXECUTABLE)'
HOST=pi@10.0.0.81
TARGET_DIR=/home/pi/Desktop/piCar
EXECUTABLE=main

# Default target to compile and build the executable
all:
	g++ -Wall -g main.cpp -o $(EXECUTABLE)

# Target to clean up the generated files
clean:
	rm -f $(EXECUTABLE) $(EXECUTABLE).o

# Target to run the program locally
run:
	./$(EXECUTABLE)
	
# Target to transfer and run on Raspberry Pi
deploy:
	scp main.cpp Makefile $(HOST):$(TARGET_DIR)
	ssh $(HOST) 'cd $(TARGET_DIR); make all; chmod +x $(EXECUTABLE); ./$(EXECUTABLE)'

