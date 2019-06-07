"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

N = 4
men_means = (42, 2358, 3200, 15145)

ind = np.arange(4)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='r')

ax.set_ylabel('Number of proteins')
ax.set_title('Proteome size by Groups')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Virus', 'Archaea', 'Bacteria', 'Eukaryotes'))

def autolabel(rects): 
  for rect in rects:
    height = rect.get_height()
    print height
    ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,  
        '%d' % int(height),
        ha='center', va='bottom')

autolabel(rects1)
plt.show()
