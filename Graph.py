import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 12
means_sales = (6226, 1521, 1842, 2051, 1728, 2138, 7479, 4434, 3615, 5472, 7224, 1812)
means_expenditure = (3808, 3373, 3965, 1098, 3046, 2258, 2084, 2799, 1649, 1116, 1431, 3532)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_sales, bar_width,
alpha=opacity,
color='b',
label='Sales')

rects2 = plt.bar(index + bar_width, means_expenditure, bar_width,
alpha=opacity,
color='g',
label='Expenditure')

plt.xlabel('Months')
plt.ylabel('Amount in GBP')
plt.title('Company Sales and Expenditure in 2018')
plt.xticks(index + bar_width, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                               'Oct', 'Nov', 'Dec'))
plt.legend()

plt.tight_layout()
plt.show()