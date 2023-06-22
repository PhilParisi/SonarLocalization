import os
import pandas as pd
import matplotlib.pyplot as plt

# Prints the folders in the current directory
def displayFolders(pathName):
    folderCount = 0
    folders = []
    # for name in os.listdir("../data/batbot_testing"):
    print("\n")
    for name in os.listdir(pathName):
        if os.path.isdir(os.path.join(pathName, name)):
            print(str(folderCount) + ": " + name)
            folders.append(name)
            folderCount += 1
    return folders

# Accesses the data folder
path = "..\\data\\batbot_testing"

# Asks the user which experiment should be parsed
folders = displayFolders(path)
userInputExpType = int(input("\nWhich experiment would you like to parse?\n"))
path = os.path.join(path, folders[userInputExpType]) 

# Asks the user which data folder should be parsed
folders = displayFolders(path)
userInput = int(input("\nWhich folder would you like to parse?\n"))
path = os.path.join(path, folders[userInput])

# Path to the folder containing CSV files
folder_path = os.path.join(path, 'CSVFiles')

# Get a list of CSV file names in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Display the available CSV files to the user
print("Which CSV do you want to plot?")
for i, file in enumerate(csv_files):
    print(f"{i+1}. {file}")

# Ask the user to choose a file to plot
choice = input("Enter the number of the file to plot: ")

# Validate the user's input
while not choice.isdigit() or int(choice) < 1 or int(choice) > len(csv_files):
    print("Invalid choice. Please enter a valid number.")
    choice = input("Enter the number of the file to plot: ")

# Get the chosen file name
chosen_file = csv_files[int(choice) - 1]

# Read the chosen file into a pandas DataFrame
file_path = os.path.join(folder_path, chosen_file)
data = pd.read_csv(file_path)

# Extract the first and second columns for plotting
x = data.iloc[:, 0]
y = data.iloc[:, 1]

# # Plot the data
plt.figure(1)
plt.plot(x, y)
plt.xlabel("index")
plt.ylabel("amplitude")
plt.title(f"Plot of {chosen_file}")


# Plot the Spectrogram
plt.figure(2)
plt.specgram(y, Fs=1/(x[1]-x[0]))  # Fs is the sampling frequency
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.title("Spectrogram")
plt.show()