<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
import csv
import os


# parseFile = "20230601_043503406"

# Function for parsing the bin files of audio recordings. 
# Contains both left and right
def bin2csv(parseFile, path):

     # opens the bin file to read the data
     # with open(parseFile + ".bin", "rb") as file:
     with open(parseFile, "rb") as file:

          # creates arrays of the data and units to get an x and y axis
          count = 0
          datapoints = []
          units = []

          # reads through entire file
          while True:
               data = file.read(1)

               if not data:
                    break

               # Adds the new read data byte into the array
               datapoints.append(int(' '.join(map(str, data))))
               units.append(count)
               count += 1


     # Splits the data into left and right ear (first half of data is right ear
     # second half is left ear)
     datapointsRight = datapoints[: count // 2]
     datapointsLeft = datapoints[count // 2 :]

     datapointsRight16 = []
     datapointsLeft16 = []

     # Because the data is 16 bit and not 8 bit, converts it to 16 bit
     for i in range(len(datapointsRight) // 2):
          datapointsRight16.append((datapointsRight[2 * i]) | (datapointsRight[2 * i + 1] << 8))
          datapointsLeft16.append((datapointsLeft[2 * i]) | (datapointsLeft[2 * i + 1] << 8))

     # Splits the units array into smaller chunks (half and a quarter)
     unitsHalf = units[: count // 2]
     unitsQuarter = units[: count // 4]

     # Creates or rewrites over a file with the file name and a right/left
     # and writes the 16 bit data into the csv
     with open(path + parseFile + "Right.csv", "w") as right:

          rightWriter = csv.writer(right, lineterminator = '\n')
          for i in range(len(datapointsRight16)):
               newRow = [unitsHalf[i], datapointsRight16[i]]
               rightWriter.writerow(newRow)

     with open(path + parseFile + "Left.csv", "w") as left:

          leftWriter = csv.writer(left, lineterminator = '\n')
          for i in range(len(datapointsLeft16)):
               newRow = [unitsHalf[i], datapointsLeft16[i]]
               leftWriter.writerow(newRow)

     # Plots data for visualization
     plt.plot(unitsQuarter, datapointsLeft16, 'bo-')
     plt.title("Amplitude vs Time (Left) " + parseFile)
     plt.xlabel("Time")
     plt.ylabel("Amplitude")
     plt.show()

     plt.plot(unitsQuarter, datapointsRight16, 'bo-')
     plt.title("Amplitude vs Time (Right) " + parseFile)
     plt.xlabel("Time")
     plt.ylabel("Amplitude")
     plt.show()

# # Plots the data
# plt.plot(unitsQuarter, datapointsLeft16, 'bo-')
# plt.title("Amplitude vs Time")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.show()

# Get the path of current working directory
path = os.getcwd()
  
# Get the list of all files and directories
# in current working directory
dir_list = os.listdir(path)

# Creates a folder within the current folder for the CSV files if it 
# doesn't exist
doesCSVExist = os.path.exists(path + "/CSVFiles")
if not doesCSVExist:
     os.mkdir(path + "/CSVFiles")

# Goes through the current folder
for file in dir_list:

     # If there is a .bin file to parse it will create a left
     # and right CSV file
     if ".bin" in file:
=======
import matplotlib.pyplot as plt
import numpy as np
import csv
import os


# parseFile = "20230601_043503406"

# Function for parsing the bin files of audio recordings. 
# Contains both left and right
def bin2csv(parseFile, path):

     # opens the bin file to read the data
     # with open(parseFile + ".bin", "rb") as file:
     with open(parseFile, "rb") as file:

          # creates arrays of the data and units to get an x and y axis
          count = 0
          datapoints = []
          units = []

          # reads through entire file
          while True:
               data = file.read(1)

               if not data:
                    break

               # Adds the new read data byte into the array
               datapoints.append(int(' '.join(map(str, data))))
               units.append(count)
               count += 1


     # Splits the data into left and right ear (first half of data is right ear
     # second half is left ear)
     datapointsRight = datapoints[: count // 2]
     datapointsLeft = datapoints[count // 2 :]

     datapointsRight16 = []
     datapointsLeft16 = []

     # Because the data is 16 bit and not 8 bit, converts it to 16 bit
     for i in range(len(datapointsRight) // 2):
          datapointsRight16.append((datapointsRight[2 * i]) | (datapointsRight[2 * i + 1] << 8))
          datapointsLeft16.append((datapointsLeft[2 * i]) | (datapointsLeft[2 * i + 1] << 8))

     # Splits the units array into smaller chunks (half and a quarter)
     unitsHalf = units[: count // 2]
     unitsQuarter = units[: count // 4]

     # Creates or rewrites over a file with the file name and a right/left
     # and writes the 16 bit data into the csv
     with open(path + parseFile + "Right.csv", "w") as right:

          rightWriter = csv.writer(right, lineterminator = '\n')
          for i in range(len(datapointsRight16)):
               newRow = [unitsHalf[i], datapointsRight16[i]]
               rightWriter.writerow(newRow)

     with open(path + parseFile + "Left.csv", "w") as left:

          leftWriter = csv.writer(left, lineterminator = '\n')
          for i in range(len(datapointsLeft16)):
               newRow = [unitsHalf[i], datapointsLeft16[i]]
               leftWriter.writerow(newRow)

     # Plots data for visualization
     plt.plot(unitsQuarter, datapointsLeft16, 'bo-')
     plt.title("Amplitude vs Time (Left) " + parseFile)
     plt.xlabel("Time")
     plt.ylabel("Amplitude")
     plt.show()

     plt.plot(unitsQuarter, datapointsRight16, 'bo-')
     plt.title("Amplitude vs Time (Right) " + parseFile)
     plt.xlabel("Time")
     plt.ylabel("Amplitude")
     plt.show()

# # Plots the data
# plt.plot(unitsQuarter, datapointsLeft16, 'bo-')
# plt.title("Amplitude vs Time")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.show()

# Get the path of current working directory
path = os.getcwd()
  
# Get the list of all files and directories
# in current working directory
dir_list = os.listdir(path)

# Creates a folder within the current folder for the CSV files if it 
# doesn't exist
doesCSVExist = os.path.exists(path + "/CSVFiles")
if not doesCSVExist:
     os.mkdir(path + "/CSVFiles")

# Goes through the current folder
for file in dir_list:

     # If there is a .bin file to parse it will create a left
     # and right CSV file
     if ".bin" in file:
>>>>>>> 9a9a2ce4fbfefadae9719f089fddd0a8862f5701
          bin2csv(file, "./CSVFiles/")