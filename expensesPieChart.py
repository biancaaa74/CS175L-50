#expensePieChart.py

import matplotlib.pyplot as plt

import numpy as np

y = np.array([1000, 250, 350, 200, 375, 800])
mylabels = ['Rent','Gas','Food','Clothing','Car Payment','Misc']

plt.pie(y, labels = mylabels)
plt.title("Monthly Expenses")
plt.show()



