import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd




import seaborn as sns
from matplotlib.ticker import MaxNLocator
custom_params = {"axes.spines.right": False, "axes.spines.top": False}
data = pd.read_csv('topk_data.csv')
sns.set_theme(style="whitegrid", palette="pastel", rc=custom_params)
sns.color_palette("flare", as_cmap=True)
ax= sns.lineplot(x='top-k', y='errorRate', data=data,
             style='dataset', hue='category',
             markers=True,dashes=False,linewidth=2,markersize=10 )
plt.xlabel("Top-k")
plt.ylabel("Category mismatch rate (%)")

ax.yaxis.grid(True) # Hide the horizontal gridlines
ax.xaxis.grid(False) # Show the vertical gridlines

plt.xlim(1, 10, 1)
#plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
