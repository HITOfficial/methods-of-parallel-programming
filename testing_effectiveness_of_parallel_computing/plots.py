import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def vcluster_time_processes():
    df_poor_mean = pd.read_csv("csv/vcluster_mean_scaling_poor.csv", delimiter=";", header=None,
                               names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_strong_mean = pd.read_csv("csv/vcluster_mean_scaling_strong.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_poor = pd.read_csv("csv/vcluster_scaling_strong.csv", delimiter=";", header=None,
                          names=['proc', 'size', 'time', 'pi'])

    df_strong = pd.read_csv("csv/vcluster_scaling_strong.csv", delimiter=";", header=None,
                            names=['proc', 'size', 'time', 'pi'])

    # calculate std time for each processor
    std_time_poor = df_poor.groupby('proc')['time'].std()
    std_time_strong = df_strong.groupby('proc')['time'].std()

    # Calculate ideal scaling time for poor scaling
    ideal_scaling_time_poor = pd.Series([df_poor_mean.loc[0, 'time']] * len(df_poor_mean['proc']))
    # Calculate ideal scaling time for strong scaling
    ideal_scaling_time_strong = df_strong_mean.loc[0, 'time'] / df_strong_mean['proc']

    plt.figure(figsize=(10, 6))
    plt.plot(df_poor_mean['proc'], df_poor_mean['time'], ':', color="grey", markersize=8)

    plt.errorbar(df_poor_mean['proc'], df_poor_mean['time'], yerr=std_time_strong, fmt='o', capsize=5, markersize=8,
                 label='std for $10^{8}$', color="blue")
    plt.plot(df_poor_mean['proc'], ideal_scaling_time_poor, 'r-', label='ideal scaling')  # Plot ideal scaling line
    plt.xlabel('number of processes')
    plt.ylabel('time [s]')
    plt.title('vCluster poor scaling time for [N] processes')
    plt.legend()
    plt.savefig("plots/vcluster_poor_scaling_time.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_strong_mean['proc'], df_strong_mean['time'], ':', color="grey", markersize=8)

    plt.errorbar(df_strong_mean['proc'], df_strong_mean['time'], yerr=std_time_poor, fmt='o', capsize=5, markersize=8,
                 label='std for $10^{8}$', color="blue")
    plt.plot(df_strong_mean['proc'], ideal_scaling_time_strong, 'r-', label='ideal scaling')  # Plot ideal scaling line
    plt.xlabel('number of processes')
    plt.ylabel('time [s]')
    plt.title('vCluster strong scaling time for [N] processes')
    plt.legend()
    plt.savefig("plots/vcluster_strong_scaling_time.png")
    plt.show()


def vcluster_speedup_processes():
    df_poor_mean = pd.read_csv("csv/vcluster_mean_scaling_poor.csv", delimiter=";", header=None,
                               names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_strong_mean = pd.read_csv("csv/vcluster_mean_scaling_strong.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    ideal_scaling_speedup_poor = pd.Series([df_poor_mean.loc[0, 'speedup']] * len(df_poor_mean['proc']))

    ideal_scaling_speedup_strong = df_strong_mean.loc[0, 'speedup'] * df_strong_mean['proc']

    plt.figure(figsize=(10, 6))
    plt.plot(df_poor_mean['proc'], df_poor_mean['speedup'], ':', color="grey")
    plt.plot(df_poor_mean['proc'], df_poor_mean['speedup'], 'o', color="blue", markersize=8, label='$10^{8}$')

    plt.plot(df_poor_mean['proc'], ideal_scaling_speedup_poor, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('speedup')
    plt.title('vCluster poor scaling speedup for [N] processes')
    plt.legend()
    plt.savefig("plots/vcluster_poor_scaling_speedup.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_strong_mean['proc'], df_strong_mean['speedup'], ':', color="grey")
    plt.plot(df_strong_mean['proc'], df_strong_mean['speedup'], 'o:', color="blue", markersize=8, label='$10^{8}$')
    plt.plot(df_strong_mean['proc'], ideal_scaling_speedup_strong, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('speedup')
    plt.title('vCluster strong scaling speedup for [N] processes')
    plt.legend()
    plt.savefig("plots/vcluster_strong_scaling_speedup.png")
    plt.show()


def vcluster_efficiency_processes():
    df_poor_mean = pd.read_csv("csv/vcluster_mean_scaling_poor.csv", delimiter=";", header=None,
                               names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_strong_mean = pd.read_csv("csv/vcluster_mean_scaling_strong.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    ideal_scaling_efficiency_poor = pd.Series([df_poor_mean.loc[0, 'efficiency']] * len(df_poor_mean['proc']))

    ideal_scaling_efficiency_strong = pd.Series([df_poor_mean.loc[0, 'efficiency']] * len(df_poor_mean['proc']
                                                                                          ))

    plt.figure(figsize=(10, 6))
    plt.plot(df_poor_mean['proc'], df_poor_mean['efficiency'], ':', color="grey")  # Plot grey dashed line
    plt.plot(df_poor_mean['proc'], df_poor_mean['efficiency'], 'o', color="blue", markersize=8, label='$10^{8}$')

    plt.plot(df_poor_mean['proc'], ideal_scaling_efficiency_poor, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('efficiency')
    plt.title('vCluster poor scaling efficiency for [N] processes')
    plt.legend()
    plt.savefig("plots/vcluster_poor_scaling_efficiency.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_strong_mean['proc'], df_strong_mean['efficiency'], ':', color="grey")  # Plot grey dashed line
    plt.plot(df_strong_mean['proc'], df_strong_mean['efficiency'], 'o:', color="blue", markersize=8, label='$10^{8}$')
    plt.plot(df_strong_mean['proc'], ideal_scaling_efficiency_strong, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('efficiency')
    plt.title('vCluster strong scaling efficiency for [N] processes')
    plt.legend()
    plt.savefig("plots/vcluster_strong_scaling_efficiency.png")
    plt.show()


def vcluster_serial_fraction_processes():
    df_poor_mean = pd.read_csv("csv/vcluster_mean_scaling_poor.csv", delimiter=";", header=None,
                               names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_strong_mean = pd.read_csv("csv/vcluster_mean_scaling_strong.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    plt.figure(figsize=(10, 6))
    plt.plot(df_poor_mean['proc'][1:], df_poor_mean['serial_fraction'][1:], ':', color="grey")  # Plot grey dashed line
    plt.plot(df_poor_mean['proc'][1:], df_poor_mean['serial_fraction'][1:], 'o', color="blue", markersize=8,
             label='$10^{8}$')

    for df, color in zip([df_poor_mean[1:]], ["blue"]):
        z = np.polyfit(df['proc'], df['serial_fraction'], 1)
        p = np.poly1d(z)
        plt.plot(df['proc'], p(df['proc']), color=color, linestyle='--', label='trend line')

    plt.xlabel('number of processes')
    plt.ylabel('serial fraction')
    plt.title('vCluster poor scaling serial fraction for [N] processes')
    plt.legend()
    plt.savefig("plots/vcluster_poor_scaling_serial_fraction.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_strong_mean['proc'][1:], df_strong_mean['serial_fraction'][1:], ':',
             color="grey")  # Plot grey dashed line
    plt.plot(df_strong_mean['proc'][1:], df_strong_mean['serial_fraction'][1:], 'o:', color="blue", markersize=8,
             label='$10^{8}$')

    for df, color in zip([df_strong_mean[1:]], ["blue"]):
        z = np.polyfit(df['proc'], df['serial_fraction'], 1)
        p = np.poly1d(z)
        plt.plot(df['proc'], p(df['proc']), color=color, linestyle='--', label='trend line')

    plt.xlabel('number of processes')
    plt.ylabel('serial fraction')
    plt.title('vCluster strong scaling serial fraction for [N] processes')
    plt.legend()
    plt.savefig("plots/vcluster_strong_scaling_serial_fraction.png")
    plt.show()


def ares_time_processes():
    df_small_mean = pd.read_csv("csv/ares_results_mean_small.csv", delimiter=";", header=None,
                                names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_medium_mean = pd.read_csv("csv/ares_results_mean_medium.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_big_mean = pd.read_csv("csv/ares_results_mean_big.csv", delimiter=";", header=None,
                              names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    df_small = pd.read_csv("csv/ares_results_small.csv", delimiter=";", header=None,
                           names=['proc', 'size', 'time', 'pi'])
    df_medium = pd.read_csv("csv/ares_results_medium.csv", delimiter=";", header=None,
                            names=['proc', 'size', 'time', 'pi'])
    df_big = pd.read_csv("csv/ares_results_big.csv", delimiter=";", header=None,
                         names=['proc', 'size', 'time', 'pi'])

    # calculate std time for each processor
    std_time_small = df_small.groupby('proc')['time'].std()
    std_time_medium = df_medium.groupby('proc')['time'].std()
    std_time_big = df_big.groupby('proc')['time'].std()

    ideal_scaling_time_small = df_small_mean.loc[0, 'time'] / df_small_mean['proc']
    ideal_scaling_time_medium = df_medium_mean.loc[0, 'time'] / df_medium_mean['proc']
    ideal_scaling_time_big = df_big_mean.loc[0, 'time'] / df_big_mean['proc']

    plt.figure(figsize=(10, 6))
    plt.plot(df_small_mean['proc'], df_small_mean['time'], ':', color="grey", markersize=8)

    plt.errorbar(df_small_mean['proc'], df_small_mean['time'], yerr=std_time_small, fmt='o', capsize=5, markersize=8,
                 label='std for $10^{8}$', color="blue")
    plt.plot(df_small_mean['proc'], ideal_scaling_time_small, 'r-', label='ideal scaling')  # Plot ideal scaling line
    plt.xlabel('number of processes')
    plt.ylabel('time [s]')
    plt.title('Aress small problem scaling time for [N] processes')
    plt.legend()
    plt.savefig("plots/ares_small_scaling_time.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_medium_mean['proc'], df_medium_mean['time'], ':', color="grey", markersize=8)

    plt.errorbar(df_medium_mean['proc'], df_medium_mean['time'], yerr=std_time_medium, fmt='o', capsize=5, markersize=8,
                 label='std for $1.4142135*10^{7}$', color="blue")
    plt.plot(df_medium_mean['proc'], ideal_scaling_time_medium, 'r-', label='ideal scaling')  # Plot ideal scaling line
    plt.xlabel('number of processes')
    plt.ylabel('time [s]')
    plt.title('Aress medium problem scaling time for [N] processes')
    plt.legend()
    plt.savefig("plots/ares_medium_scaling_time.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_big_mean['proc'], df_big_mean['time'], ':', color="grey", markersize=8)

    plt.errorbar(df_big_mean['proc'], df_big_mean['time'], yerr=std_time_big, fmt='o', capsize=5, markersize=8,
                 label='std for $2*10^{9}$', color="blue")
    plt.plot(df_big_mean['proc'], ideal_scaling_time_big, 'r-', label='ideal scaling')  # Plot ideal scaling line
    plt.xlabel('number of processes')
    plt.ylabel('time [s]')
    plt.title('Aress big problem scaling time for [N] processes')
    plt.legend()
    plt.savefig("plots/ares_big_scaling_time.png")
    plt.show()


def ares_speedup_processes():
    df_small_mean = pd.read_csv("csv/ares_results_mean_small.csv", delimiter=";", header=None,
                                names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_medium_mean = pd.read_csv("csv/ares_results_mean_medium.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_big_mean = pd.read_csv("csv/ares_results_mean_big.csv", delimiter=";", header=None,
                              names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    ideal_scaling_speedup = df_small_mean.loc[0, 'speedup'] * df_small_mean[
        'proc']  # ideal scaling is the same for each problem size

    plt.figure(figsize=(10, 6))

    plt.plot(df_small_mean['proc'], ideal_scaling_speedup, 'r-', label='ideal scaling')
    plt.plot(df_small_mean['proc'], df_small_mean['speedup'], ':o', color="green", markersize=8, label='$10^{5}$')
    plt.plot(df_medium_mean['proc'], df_medium_mean['speedup'], ':o', color="blue", markersize=8,
             label='$1.4142135*10^{7}$')
    plt.plot(df_big_mean['proc'], df_big_mean['speedup'], ':o', color="orange", markersize=8, label='$2*10^{9}$')

    plt.xlabel('number of processes')
    plt.ylabel('speedup')
    plt.title('Ares scaling speedup for [N] processes')
    plt.legend()
    plt.savefig("plots/ares_scaling_speedup.png")
    plt.show()


def ares_efficiency_processes():
    df_small_mean = pd.read_csv("csv/ares_results_mean_small.csv", delimiter=";", header=None,
                                names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_medium_mean = pd.read_csv("csv/ares_results_mean_medium.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_big_mean = pd.read_csv("csv/ares_results_mean_big.csv", delimiter=";", header=None,
                              names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    ideal_scaling_efficiency = pd.Series([df_small_mean.loc[0, 'efficiency']] * len(df_small_mean['proc']
                                                                                    ))  # ideal scaling is the same for each problem size

    plt.figure(figsize=(10, 6))

    plt.plot(df_small_mean['proc'], ideal_scaling_efficiency, 'r-', label='ideal scaling')
    plt.plot(df_small_mean['proc'], df_small_mean['efficiency'], ':o', color="green", markersize=8, label='$10^{5}$')
    plt.plot(df_medium_mean['proc'], df_medium_mean['efficiency'], ':o', color="blue", markersize=8,
             label='$1.4142135*10^{7}$')
    plt.plot(df_big_mean['proc'], df_big_mean['efficiency'], ':o', color="orange", markersize=8, label='$2*10^{9}$')

    plt.xlabel('number of processes')
    plt.ylabel('efficiency')
    plt.title('Ares scaling efficiency for [N] processes')
    plt.legend()
    plt.savefig("plots/ares_scaling_efficiency.png")
    plt.show()


def ares_serial_fraction_processes():
    df_small_mean = pd.read_csv("csv/ares_results_mean_small.csv", delimiter=";", header=None,
                                names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_medium_mean = pd.read_csv("csv/ares_results_mean_medium.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_big_mean = pd.read_csv("csv/ares_results_mean_big.csv", delimiter=";", header=None,
                              names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    plt.figure(figsize=(10, 6))

    plt.plot(df_small_mean['proc'][1:], df_small_mean['serial_fraction'][1:], ':o', color="green", markersize=8,
             label='$10^{5}$')
    plt.plot(df_medium_mean['proc'][1:], df_medium_mean['serial_fraction'][1:], ':o', color="blue", markersize=8,
             label='$1.4142135*10^{7}$')
    plt.plot(df_big_mean['proc'][1:], df_big_mean['serial_fraction'][1:], ':o', color="orange", markersize=8,
             label='$2*10^{9}$')

    # Adding trend lines
    for df, color in zip([df_small_mean[1:], df_medium_mean[1:], df_big_mean[1:]], ["green", "blue", "orange"]):
        z = np.polyfit(df['proc'], df['serial_fraction'], 1)
        p = np.poly1d(z)
        plt.plot(df['proc'], p(df['proc']), color=color, linestyle='--', label='trend line')

    plt.xlabel('number of processes')
    plt.ylabel('serial fraction')
    plt.title('Ares scaling serial fraction for [N] processes')
    plt.legend()
    plt.savefig("plots/ares_scaling_serial_fraction.png")
    plt.show()


def update_result_csv(path, result_path):
    df = pd.read_csv(path, delimiter=";", header=None, names=['proc', 'size', 'time', 'pi'])
    df_mean = df.groupby('proc', as_index=False).mean()
    df_mean['proc'] = df_mean['proc'].astype(int)
    df_mean['size'] = df_mean['size'].astype(int)
    df_mean['speedup'] = df_mean['time'].iloc[0] / df_mean['time']
    df_mean['efficiency'] = df_mean['speedup'] / df_mean['proc']
    df_mean['serial_fraction'] = df_mean['time'] / (df_mean['proc'] * df_mean['time'].iloc[0])
    columns_ordered = ['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction']
    df_mean = df_mean[columns_ordered]
    df_mean.to_csv(result_path, index=False, sep=";", header=False)


if __name__ == "__main__":
    update_result_csv("csv/vcluster_scaling_poor.csv", "csv/vcluster_mean_scaling_poor.csv")
    update_result_csv("csv/vcluster_scaling_strong.csv", "csv/vcluster_mean_scaling_strong.csv")
    update_result_csv("csv/ares_results_small.csv", "csv/ares_results_mean_small.csv")
    update_result_csv("csv/ares_results_medium.csv", "csv/ares_results_mean_medium.csv")
    update_result_csv("csv/ares_results_big.csv", "csv/ares_results_mean_big.csv")

    vcluster_time_processes()
    vcluster_speedup_processes()
    vcluster_efficiency_processes()
    vcluster_serial_fraction_processes()

    ares_time_processes()
    ares_speedup_processes()
    ares_efficiency_processes()
    ares_serial_fraction_processes()
