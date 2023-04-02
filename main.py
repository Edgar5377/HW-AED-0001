import csv
import pandas as pd
import matplotlib.pyplot as plt


x = []
y1 = []
y2 = []

with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  
    for row in csvreader:
        x.append(int(row[0]))
        y1.append(int(row[1]))
        y2.append(int(row[2]))



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# plot data with lines and markers
ax1.semilogy(x, y1, linestyle='-', marker='o', color='blue', label='Bubble Sort')
ax1.semilogy(x, y2, linestyle='--', marker='o', color='red', label='Heap Sort')

# add legend and labels to first subplot
ax1.legend()
ax1.set_title('Sorting Algorithm Comparison')
ax1.set_xlabel('n_values')
ax1.set_ylabel('Time (ms)')

# read CSV data into a pandas DataFrame
data = pd.read_csv('data.csv')

# create table with CSV data in second subplot
table = ax2.table(cellText=data.values, colLabels=data.columns, loc='center')
table.auto_set_font_size(False)

table.scale(1.5, 2)

table.set_fontsize(13)
ax2.axis('off')
ax2.set_title('Running Time')

plt.subplots_adjust(wspace=0.3)


plt.show()