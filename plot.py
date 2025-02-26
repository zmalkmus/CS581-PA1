import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'results.csv'
df = pd.read_csv(csv_file, header=None, names=['file', 'file size', 'r', 'time'])

# Exclude rows where n is 10000000.
# df = df[df['file size'] != 1000]
# df = df[df['file size'] != 10000]
# df = df[df['file size'] != 100000]
# df = df[df['file size'] != 1000000]
# df = df[df['file size'] != 10000000]

plt.figure(figsize=(10, 6))

for r_val, group in df.groupby('r'):
    plt.plot(group['file size'], group['time'], marker='o', label=f'r = {r_val}')

plt.xlabel('File Size (integers)')
plt.ylabel('Time')
# plt.xscale('log')
# plt.yscale('log')
plt.title('Time vs File Size for Different r')
plt.legend()
plt.grid(True, which="both", ls="--")

plt.show()
