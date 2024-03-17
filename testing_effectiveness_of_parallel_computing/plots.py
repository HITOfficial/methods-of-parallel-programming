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
                 label='std for 10e^8', color="blue")
    plt.plot(df_poor_mean['proc'], ideal_scaling_time_poor, 'r-', label='ideal scaling')  # Plot ideal scaling line
    plt.xlabel('number of processes')
    plt.ylabel('time [s]')
    plt.title('vCluster poor scaling time for [N] processes')
    plt.legend()
    plt.savefig("vcluster_poor_scaling_time.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_strong_mean['proc'], df_strong_mean['time'], ':', color="grey", markersize=8)

    plt.errorbar(df_strong_mean['proc'], df_strong_mean['time'], yerr=std_time_poor, fmt='o', capsize=5, markersize=8,
                 label='std for 10e^8', color="blue")
    plt.plot(df_strong_mean['proc'], ideal_scaling_time_strong, 'r-', label='ideal scaling')  # Plot ideal scaling line
    plt.xlabel('number of processes')
    plt.ylabel('time [s]')
    plt.title('vCluster strong scaling time for [N] processes')
    plt.legend()
    plt.savefig("vcluster_strong_scaling_time.png")
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
    plt.plot(df_poor_mean['proc'], df_poor_mean['speedup'], 'o', color="blue", markersize=8, label='10e^8')

    plt.plot(df_poor_mean['proc'], ideal_scaling_speedup_poor, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('speedup')
    plt.title('vCluster poor scaling speedup for [N] processes')
    plt.legend()
    plt.savefig("vcluster_poor_scaling_speedup.png")
    plt.show()


    plt.figure(figsize=(10, 6))
    plt.plot(df_strong_mean['proc'], df_strong_mean['speedup'], ':', color="grey")
    plt.plot(df_strong_mean['proc'], df_strong_mean['speedup'], 'o:', color="blue", markersize=8, label='10e^8')
    plt.plot(df_strong_mean['proc'], ideal_scaling_speedup_strong, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('speedup')
    plt.title('vCluster strong scaling speedup for [N] processes')
    plt.legend()
    plt.savefig("vcluster_strong_scaling_speedup.png")
    plt.show()


def vcluster_efficiency_processes():
    df_poor_mean = pd.read_csv("csv/vcluster_mean_scaling_poor.csv", delimiter=";", header=None,
                               names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_strong_mean = pd.read_csv("csv/vcluster_mean_scaling_strong.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    ideal_scaling_efficiency_poor = pd.Series([df_poor_mean.loc[0, 'efficiency']] * len(df_poor_mean['proc']))

    ideal_scaling_efficiency_strong = pd.Series([df_poor_mean.loc[0, 'efficiency']] * len(df_poor_mean['proc']))

    plt.figure(figsize=(10, 6))
    plt.plot(df_poor_mean['proc'], df_poor_mean['efficiency'], ':', color="grey")  # Plot grey dashed line
    plt.plot(df_poor_mean['proc'], df_poor_mean['efficiency'], 'o', color="blue", markersize=8, label='10e^8')

    plt.plot(df_poor_mean['proc'], ideal_scaling_efficiency_poor, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('efficiency')
    plt.title('vCluster poor scaling efficiency for [N] processes')
    plt.legend()
    plt.savefig("vcluster_poor_scaling_efficiency.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_strong_mean['proc'], df_strong_mean['efficiency'], ':', color="grey")  # Plot grey dashed line
    plt.plot(df_strong_mean['proc'], df_strong_mean['efficiency'], 'o:', color="blue", markersize=8, label='10e^8')
    plt.plot(df_strong_mean['proc'], ideal_scaling_efficiency_strong, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('efficiency')
    plt.title('vCluster strong scaling efficiency for [N] processes')
    plt.legend()
    plt.savefig("vcluster_strong_scaling_efficiency.png")
    plt.show()


def vcluster_serial_fraction_processes():
    df_poor_mean = pd.read_csv("csv/vcluster_mean_scaling_poor.csv", delimiter=";", header=None,
                               names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])
    df_strong_mean = pd.read_csv("csv/vcluster_mean_scaling_strong.csv", delimiter=";", header=None,
                                 names=['proc', 'size', 'time', 'pi', 'speedup', 'efficiency', 'serial_fraction'])

    ideal_scaling_efficiency_poor = pd.Series(
        df_poor_mean['time'].iloc[0] / (df_poor_mean['proc'] * df_poor_mean['time'].iloc[0]))
    ideal_scaling_efficiency_strong = pd.Series(
        df_poor_mean['time'].iloc[0] / (df_strong_mean['proc'] * df_strong_mean['time'].iloc[0]))

    plt.figure(figsize=(10, 6))
    plt.plot(df_poor_mean['proc'], df_poor_mean['serial_fraction'], ':', color="grey")  # Plot grey dashed line
    plt.plot(df_poor_mean['proc'], df_poor_mean['serial_fraction'], 'o', color="blue", markersize=8, label='10e^8')

    plt.plot(df_poor_mean['proc'], ideal_scaling_efficiency_poor, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('serial fraction')
    plt.title('vCluster poor scaling serial fraction for [N] processes')
    plt.legend()
    plt.savefig("vcluster_poor_scaling_serial_fraction.png")
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_strong_mean['proc'], df_strong_mean['serial_fraction'], ':', color="grey")  # Plot grey dashed line
    plt.plot(df_strong_mean['proc'], df_strong_mean['serial_fraction'], 'o:', color="blue", markersize=8, label='10e^8')
    plt.plot(df_strong_mean['proc'], ideal_scaling_efficiency_strong, 'r-', label='ideal scaling')
    plt.xlabel('number of processes')
    plt.ylabel('serial fraction')
    plt.title('vCluster strong scaling serial fraction for [N] processes')
    plt.legend()
    plt.savefig("vcluster_strong_scaling_serial_fraction.png")
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
    vcluster_time_processes()
    vcluster_speedup_processes()
    vcluster_efficiency_processes()
    vcluster_serial_fraction_processes()
