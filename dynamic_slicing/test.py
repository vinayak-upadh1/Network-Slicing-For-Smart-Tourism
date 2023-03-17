from pandas import*
import matplotlib.pyplot as plt

data  = read_csv("IIIT_Dharwad.csv",skiprows=9);
# print(data);
data = data[[' channelWidth',' txPower']];
print(data);
x = data[' channelWidth'].tolist()[10:100];
y = data[' txPower'].tolist()[10:100];
tempxy = [list((float(d[0]), float(d[1]))) for d in zip(x,y)]
# tempxy.sort()
x = y = []
for temp in tempxy:
    # print(temp)
    x.append(temp[0])
    y.append(temp[1])

plt.plot(x,y,".r-");
# plt.plot(x,y,"og");
plt.xlim([0,25])
plt.ylim([0,25])
# plt.xticks(ticks=[],labels=[])
# plt.yticks(ticks=[],labels=[])
# naming the x axis
plt.xlabel(' BandWidth')
# naming the y axis
plt.ylabel(' Transmission Power')

# giving a title to my graph
plt.title('Graph showing relation b/w Bandwidth and Transmission Power')

# function to show the plot
plt.show()

