import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import shutil

# Function for parsing the bin files of audio recordings. 
# Contains both left and right
def bin2csv(parseFile, destination, desiredEarData, path):

    # opens the bin file to read the data
    # with open(parseFile + ".bin", "rb") as file:
    with open(path + parseFile, "rb") as file:

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

    fileNameNoBin = parseFile[: len(parseFile) - 4]

    # Creates or rewrites over a file with the file name and a right/left
    # and writes the 16 bit data into the csv
    if desiredEarData % 2 == 0:
        with open(destination + fileNameNoBin + "Right.csv", "w") as right:

            rightWriter = csv.writer(right, lineterminator = '\n')
            for i in range(len(datapointsRight16)):
                newRow = [unitsHalf[i], datapointsRight16[i]]
                rightWriter.writerow(newRow)

    if desiredEarData < 2:
        with open(destination + fileNameNoBin + "Left.csv", "w") as left:

            leftWriter = csv.writer(left, lineterminator = '\n')
            for i in range(len(datapointsLeft16)):
                newRow = [unitsHalf[i], datapointsLeft16[i]]
                leftWriter.writerow(newRow)

    # Plots data for visualization uncomment if you want to visualize
    # plt.plot(unitsQuarter, datapointsLeft16, 'bo-')
    # plt.title("Amplitude vs Time (Left) " + parseFile)
    # plt.xlabel("Time")
    # plt.ylabel("Amplitude")
    # plt.show()

    # plt.plot(unitsQuarter, datapointsRight16, 'bo-')
    # plt.title("Amplitude vs Time (Right) " + parseFile)
    # plt.xlabel("Time")
    # plt.ylabel("Amplitude")
    # plt.show()

def getEarData():
    userInput = int(input("\nWhich ears would you like to get data for? 0: Both, 1: Left, 2: Right\n"))
    if userInput == 0 or userInput == 1 or userInput == 2:
        return userInput, True
    else:
        return userInput, False

# This method deletes the contents of the folder provided as a parameter
def deleteFolderContents(deleteFolder):
    # Code from:
    # https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder
    folder = deleteFolder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    # End of stackoverflow code

# Prints the folders in the current directory
folderCount = 0
folders = []
for name in os.listdir("."):
    if os.path.isdir(name):
        print(str(folderCount) + ": " + name)
        folders.append(name)
        folderCount += 1

userInput = int(input("\nWhich folder would you like to parse?\n"))
# path = "./" + folders[userInput]
# print(path)

# Get the path of current working directory
currentPath = os.getcwd()
path = currentPath + "\\" + folders[userInput]
print(path)
  
# Get the list of all files and directories
# in current working directory
dir_list = os.listdir(path)

print(dir_list)

# Creates a folder within the current folder for the CSV files if it 
# doesn't exist
doesCSVExist = os.path.exists(path + "/CSVFiles")
if not doesCSVExist:
    os.mkdir(path + "/CSVFiles")
else:
    # Deletes content inside to make new files
    deleteFolderContents(path + "/CSVFiles/")

# Asks the user for which data that would like to get
userInput, validUserInput = getEarData()

while not validUserInput:
    print("Please input valid value")
    userInput, validUserInput = getEarData()

# Goes through the current folder
for file in dir_list:

    # If there is a .bin file to parse it will create a left
    # and right CSV file
    if ".bin" in file:
        bin2csv(file, path + "/CSVFiles/", userInput, path + "\\")