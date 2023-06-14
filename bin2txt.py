import matplotlib.pyplot as plt
import numpy as np
import csv


parseFile = "20230601_043503406"

with open(parseFile + ".bin", "rb") as file:

     # data = file.read(8)
     # print("\n")
     # print(data)
     # print(' '.join(map(str, data)))
     # everyOther = True
     count = 0
     datapoints = []
     units = []

     while True:
          data = file.read(1)

          if not data:
               break

          # print("\n")
          # # print(data)


          # if (everyOther):
          #      print(' '.join(map(str, data)))
          #      # datapoints.append(int(' '.join(map(str, data))))
          #      datapoints.append(int(' '.join(map(str, data))))
          #      everyOther = False
          #      units.append(count)
          #      count += 1
          # else:
          #      print(' '.join(map(str, data)))
          #      everyOther = True

          # print(' '.join(map(str, data)))
          datapoints.append(int(' '.join(map(str, data))))
          units.append(count)
          count += 1



datapointsRight = datapoints[: count // 2]
datapointsLeft = datapoints[count // 2 :]

datapointsRight16 = []
datapointsLeft16 = []

for i in range(len(datapointsRight) // 2):
     datapointsRight16.append((datapointsRight[2 * i] << 8) | (datapointsRight[2 * i + 1]))
     datapointsLeft16.append((datapointsLeft[2 * i] << 8) | (datapointsLeft[2 * i + 1]))


unitsHalf = units[: count // 2]
unitsQuarter = units[: count // 4]

# print(unitsHalf)

# for i in range(len(datapointsLeft)):
#      print(i)

# print(count // 2)

with open(parseFile + "Right.csv", "w") as right:

     rightWriter = csv.writer(right, lineterminator = '\n')
     for i in range(len(datapointsRight16)):
          newRow = [unitsHalf[i], datapointsRight16[i]]
          rightWriter.writerow(newRow)

with open(parseFile + "Left.csv", "w") as left:

     leftWriter = csv.writer(left, lineterminator = '\n')
     for i in range(len(datapointsLeft16)):
          newRow = [unitsHalf[i], datapointsLeft16[i]]
          leftWriter.writerow(newRow)



# print(datapointsRight)


# print(datapoints)
# print(count)
# print(len(datapointsRight))
# print(datapointsRight == datapointsLeft)
# print(datapointsRight[1000])
# print(datapointsLeft[1000])

plt.plot(unitsQuarter, datapointsRight16)
# plt.axis("equal")
# plt.xticks(np.arange(0, max(datapoints)+1, 10.0))
plt.title("Amplitude vs Time")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()