
import matplotlib.pyplot as plt
import numpy as np

# Part 3 - Provo River Streamflow Data

# Read the Provo River CSV file
data = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv',
                     delimiter=',', skip_header=1, dtype=str)

# Separate dates and streamflow values
x = np.array(data[:, 0], dtype='datetime64[m]')
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

# Sort the measurements by date and time
order = np.argsort(x)

x = x[order]
y_1 = y_1[order]
y_2 = y_2[order]
y_3 = y_3[order]
y_4 = y_4[order]
y_5 = y_5[order]

# Plot streamflow for all five sites
plt.figure(figsize=(10, 6))

plt.plot(x, y_1, color='purple', label='10163000')
plt.plot(x, y_2, color='teal', label='10155200')
plt.plot(x, y_3, color='green', label='10155500')
plt.plot(x, y_4, color='orange', label='10154200')
plt.plot(x, y_5, color='orangered', label='10155000')

plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')

plt.legend(title='Site Numbers', loc='upper right')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
