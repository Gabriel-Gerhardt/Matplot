import numpy as np
import matplotlib.pyplot as plt

#Individual data points in a grafic

x_data = np.random.random(50) *1000
y_data =np.random.random(50)*1000

print(x_data)
plt.scatter(x_data,y_data, s=50,edgecolors="black")
plt.show()