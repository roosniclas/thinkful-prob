import pandas as pd
import os
import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

df = pd.DataFrame(x, columns = ['Occurences'])

freq = pd.DataFrame(df['Occurences'].value_counts(sort = False))

freq['Frequency'] = freq.apply(lambda x : x / freq['Occurences'].sum())

print('Frequency count:')
print(freq)

boxplot = df.plot(kind = 'box', return_type='axes')
boxplot_fig = boxplot.get_figure()
boxplot_fig.savefig('boxplot')

histogram = df.plot(kind='hist', align = 'left')
histogram_fig = histogram.get_figure()
histogram_fig.savefig('histogram')

plt.figure()  
qq_plot = stats.probplot(df.Occurences , dist="norm", plot=plt)
plt.savefig('qq_plot')

plt.close()

