import matplotlib.pyplot as plt
import numpy as np

gaussian_numbers = np.random.randn(1000)
plt.hist(gaussian_numbers)
#df.hist() also works where df is a dataframe
df.plot(kind='scatter', x='SPY', y='XOM')
beta_XOM, alpha_XOM = np.polyfit(df['SPY'], df['XOM'], 1)
plt.plot(df['SPY'], beta_XOM * df['SPY'] + alpha_XOM, '-', color='r')
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
ply.show()

