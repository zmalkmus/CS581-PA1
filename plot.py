import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to your CSV file.
csv_file = 'results.csv'  # Update this path as needed

# Read the CSV file into a DataFrame.
df = pd.read_csv(csv_file, header=None, names=['file', 'n', 'k', 'time'])

# Exclude rows where n is 10000000.
df = df[df['n'] != 1000]
df = df[df['n'] != 10000]
df = df[df['n'] != 100000]
df = df[df['n'] != 1000000]

plt.figure(figsize=(10, 6))

# Create a line plot for each unique 'k' value.
for k_val, group in df.groupby('k'):
    plt.plot(group['n'], group['time'], marker='o', label=f'k = {k_val}')

# Configure the plot with logarithmic scales for both axes.
plt.xlabel('n')
plt.ylabel('Time')
# plt.xscale('log')
# plt.yscale('log')
plt.legend()
plt.grid(True, which="both", ls="--")

# Display the plot.
plt.show()
