
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file and organize the data
def load_streamflow(filename):
    data = np.genfromtxt(filename, delimiter=',',
                         skip_header=1, dtype=str)

    dates = np.array(data[:, 0], dtype='datetime64[m]')
    flows = data[:, 1:6].astype(float)

    order = np.argsort(dates)
    dates = dates[order]
    flows = flows[order]

    return dates, flows


# Create the graph for all five sites
def plot_streamflow(dates, flows, sites):
    plt.figure(figsize=(10, 6))

    colors = ['purple', 'teal', 'green', 'orange', 'orangered']

    for i in range(5):
        plt.plot(dates, flows[:, i], color=colors[i], label=sites[i])

    plt.title('Provo River Streamflow Data (2021)')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.legend(title='Site Numbers', loc='upper right')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


# Main program
sites = ['10163000', '10155200', '10155500', '10154200', '10155000']

dates, flows = load_streamflow('June-2021-Provo-River-Streamflow-Rates.csv')
plot_streamflow(dates, flows, sites)
