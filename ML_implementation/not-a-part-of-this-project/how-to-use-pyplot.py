import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

space = np.linspace(0, 1, 1000)
fig, ax = plt.subplots(figsize = (20,10))
for a, b in [(0,0), (2, 8), (10, 40), (20, 80), (40, 160)]:
    ax.plot(space, stats.beta.pdf(space, a+1, b+1),label=f'a={a}, b={b}')
ax.legend(prop={'size': 20})
plt.show()