import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Generate random numbers from a gamma distribution with shape parameter 'a=5'
data_gamma = gamma.rvs(a=5, size=10000)

ax = sns.distplot(data_gamma,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15, 'alpha': 1})
ax.set(xlabel='Gamma Distribution', ylabel='Frequency')

plt.show()  # Show the plot
