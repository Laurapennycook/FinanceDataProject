import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                               'Oct', 'Nov', 'Dec')
y_pos = np.arange(len(objects))
performance = [2418, -1852, -2123, 953, -1318, -120, 5395, 1635, 1966, 4356, 5793, -1720]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Amount in GBP')
plt.xlabel('Months')
plt.title('Company Monthly Profits 2018')

plt.show()