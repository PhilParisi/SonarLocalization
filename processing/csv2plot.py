import os
import pandas as pd
import matplotlib.pyplot as plt

# Path to the folder containing CSV files
folder_path = 'CSVFiles'

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

# Plot the data
plt.plot(x, y)
plt.xlabel("index")
plt.ylabel("amplitude")
plt.title(f"Plot of {chosen_file}")
plt.show()

