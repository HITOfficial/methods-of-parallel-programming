import pandas as pd
import matplotlib.pyplot as plt

ec2_data = [
    {'nCores': 16, 'dataSize': 1,'confId': 'szeregowe', 'time': 22566},
    {'nCores': 16, 'dataSize': 5,'confId': 'szeregowe', 'time': 89651},
    {'nCores': 16, 'dataSize': 10,'confId': 'szeregowe', 'time': 131805},
    {'nCores': 2, 'dataSize': 1, 'confId': 'szeregowe', 'time': 35591},
    {'nCores': 2, 'dataSize': 5,'confId': 'szeregowe', 'time': 114374},
    {'nCores': 2, 'dataSize': 10,'confId': 'szeregowe', 'time': 143927},
]

emr_data = [
    {'nCores': 2, 'confId': 'słabsze', 'dataSize': 1, 'time': 130332},
    {'nCores': 2, 'confId': 'słabsze', 'dataSize': 5, 'time': 589789},
    {'nCores': 2, 'confId': 'słabsze', 'dataSize': 10, 'time': 1116105},
    {'nCores': 2, 'confId': 'mocniejsze', 'dataSize': 1, 'time': 73062},
    {'nCores': 2, 'confId': 'mocniejsze', 'dataSize': 5, 'time': 257478},
    {'nCores': 2, 'confId': 'mocniejsze', 'dataSize': 10, 'time': 499033},
    {'nCores': 16, 'confId': 'słabsze', 'dataSize': 1, 'time': 77512},
    {'nCores': 16, 'confId': 'słabsze', 'dataSize': 5, 'time': 300353},
    {'nCores': 16, 'confId': 'słabsze', 'dataSize': 10, 'time': 610725},
    {'nCores': 16, 'confId': 'mocniejsze', 'dataSize': 1, 'time': 53060},
    {'nCores': 16, 'confId': 'mocniejsze', 'dataSize': 5, 'time': 135270},
    {'nCores': 16, 'confId': 'mocniejsze', 'dataSize': 10, 'time': 239418},
]

all_data = emr_data

df = pd.DataFrame(all_data)

grouped = df.groupby(['dataSize', 'confId', 'nCores'])

mean_times = grouped['time'].mean()

fig, axs = plt.subplots(2, 2, figsize=(15, 10))

count = 0
for (size, conf), data in mean_times.groupby(level=[0, 1]):
    ax = axs[count//2, count%2]
    ax.plot(data.index.get_level_values('nCores'), data.values, label=f"{size}GB")
    ax.set_title(f"Średni czas obliczeń dla {size}GB ({conf})")
    ax.legend()
    ax.set_xlabel("Liczba rdzeni")
    ax.set_ylabel("Średni czas obliczeń [ms]")
    count += 1

plt.tight_layout()
plt.show()