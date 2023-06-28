import os
import pandas as pd
import matplotlib.pyplot as plt
import bin2csv
import numpy as np

# Creates the Plots folder in the provided path
def createPlotsFolder(path):
    # Creates a folder within the current folder for the plot files if it 
    # doesn't exist
    doesPlotFolderExist = os.path.exists(path + "\\Plots")
    if not doesPlotFolderExist:
        os.mkdir(path + "\\Plots")
    else:
        # Deletes content inside to make new files
        bin2csv.deleteFolderContents(path + "\\Plots\\")

# This function creates the spectrograms and the plots for the
# provided CSV file
def createPlot(path, csvFile):
    # Create the folder that will contain the plots
    plotsPath = os.path.join(path, "Plots")

    # Path to the CSVs
    csvFolderPath = os.path.join(bin2csv.path, "CSVFiles")
    csvPath = os.path.join(csvFolderPath, csvFile)

    # Read the chosen file into a pandas DataFrame
    data = pd.read_csv(csvPath)

    # Extract the first and second columns for plotting
    x = data.iloc[:, 0]
    y = data.iloc[:, 1] # * 1000

    # Plot the data
    plt.plot(x, y)
    plt.xlabel("index")
    plt.ylabel("amplitude")
    plt.title(f"Plot of {csvFile}")
    plt.savefig(plotsPath + "\\" + ("Plot " + csvFile[1:-4]))
    plt.clf()

    # Plot the Spectrogram
    plt.specgram(y, Fs=1.05 * 1000)  # Fs is the sampling frequency (this is in kHz instead of Hz)
    # Fs = 1.05 * 1000000 for hz
    plt.xlabel("Time")
    plt.ylabel("Frequency (kHz)")
    plt.title("Spectrogram")
    plt.colorbar(label='Intensity (dB)')
    plt.savefig(plotsPath + "\\" + ("Spectrogram " + csvFile[1:-4]))
    plt.clf()


# Path to the folder containing CSV files
folder_path = os.path.join(bin2csv.path, 'CSVFiles')

# Get a list of CSV file names in the folder
csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

# Creates the Plots folder and populates it with spectrograms and plots
createPlotsFolder(bin2csv.path)
for csv_file in csv_files:
    createPlot(bin2csv.path, csv_file)