import matplotlib.pyplot as plt
import csv

x = []
y = []
file_path = r"/Users/andynur/Dev/pylearn/materi-10-file/anime.csv"
with open(file_path,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')    
    for row in plots:
     if row[0] != "No":
        x.append(row[2])
        y.append(float(row[3]))

plt.bar(x, y, color = 'g', width = 0.72, label = "Rating")
plt.xlabel('Anime')
plt.ylabel('Rating')
plt.title('Rating dari anime berbeda')
plt.legend()
plt.show()
