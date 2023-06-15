# Serial Communications Logging Script
# GOAL: connect to arduino via serial connection, then log the incoming data to a .csv file

import datetime
import serial
import csv
import os


# connect via serial port (if you are on a PC, you can check this in device manager)
ser = serial.Serial('COM5', 115200) 	# likely need to change the com port number and serial rate

# place to save the raw data files
directory_path = "raw_data"

# check if the directory exists
if not os.path.exists(directory_path):
    # create the directory
    os.makedirs(directory_path)
    print("Directory created: ", directory_path)

# for naming the csv, pull in the current datetime
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

csv_filename = directory_path + "\logged_gps_" + formatted_datetime + ".csv"
print("Saving csv as " + csv_filename + " in the current directory")

print("logging data... use 'ctrl+c' to stop")

# open csv in append mode ('a')
with open(csv_filename, 'a', newline='') as file:

	writer = csv.writer(file)

	try: 		# allows us to throw the keyboard exception properly

		while True:

			# check if serial data is available (are bytes in serial buffer?)
			if ser.in_waiting:
			
				# grab the data from the serial buffer
				data = ser.readline().decode().rstrip()
	
				# print data as an output (for debugging... comment out later)
				#print(f"Received data: {data}")

				# write the data into a new line of the csv
				writer.writerow([data])

	except KeyboardInterrupt:
		print("Logging stopped by user!")

ser.close()