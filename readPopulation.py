import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Import graphics module


df = pd.read_csv('populations.txt',
                    sep = '\t',
                    names = ['year', 'hare', 'lynx', 'carrot'],
                    index_col = 'year',
                    skiprows = 1)

df['hare.grad'] = np.gradient(df['hare'].values)

# ### PLOTING
fig = plt.figure()
line_hare, line_lynx = plt.plot(df.index, 'hare.grad', 'lynx', data = df, linewidth = 2.) # Plot using data argument
plt.setp(line_hare, color = 'cornflowerblue') # Set color of hare population data's gradient
plt.setp(line_lynx, color = 'slateblue') # Set color of lynx population's data

# Description for legend
line_hare.set_label('Change in hare population')
line_lynx.set_label('Population of lynxes')

# Plot figure
plt.legend()
plt.savefig("corr.png")
