import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_latency_bar(a,b,c,d):
    x = a['c1']
    x_axis = np.arange(len(x))
    y1 = a['c3']
    y2 = b['c3']
    y3 = c['c3']
    y4 = d['c3']
    plt.figure(figsize=(18, 6))  # Twice as wide, adjust the width and height as needed

    plt.plot(y1, label='standard using 1 node')
    plt.plot(y2, label='standard using 2 nodes')
    plt.plot(y3, label='synchronous using 1 node')
    plt.plot(y4, label='synchronous using 2 nodes')

    plt.xticks(x_axis, x)
    plt.xlabel("Message size [B]")
    plt.ylabel("Bandwidth [MB/s]")
    plt.title("Bandwitch for different messages sizes and different message transfer methods")
    plt.legend()
    save_path = "plots/latency_plot_for_all.png"
    plt.savefig(save_path)
    plt.show()

def read_data(file_path):
    data = pd.read_csv(file_path,delimiter=";", header=None, names=['c1', 'c2', 'c3'])
    return data

# Wczytanie danych z różnych przypadków
standard_case1_data = read_data('standard_case1.csv')
standard_case2_data = read_data('standard_case2.csv')
sync_case1_data = read_data('synchronous_case1.csv')
sync_case2_data = read_data('synchronous_case2.csv')

# Lista danych z różnych przypadków
data_list = [standard_case1_data, standard_case2_data, sync_case1_data, sync_case2_data]

plot_latency_bar(standard_case1_data, standard_case2_data, sync_case1_data, sync_case2_data)

# Wykres kolumnowy dla latencji i wielkości wiadomości
