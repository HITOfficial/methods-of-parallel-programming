import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv('../csv/matrix_addition.csv', sep=';')

fig, axs = plt.subplots(2, 1, figsize=(14, 10))
sns.set_theme(style="whitegrid")

sns.lineplot(data=df, x='n', y='elapsed_time', hue='threads_per_block', marker='o')

sns.lineplot(data=df, x='n', y='elapsed_time', hue='threads_per_block', marker='o', ax=axs[0])
axs[0].set_xscale('log', base=2)
axs[0].set_yscale('log')
axs[0].set_title('Elapsed Time vs. Problem Size for Different Threads Per Block')
axs[0].set_xlabel('Problem Size (n)')
axs[0].set_ylabel('Elapsed Time (s)')
axs[0].legend(title='Threads Per Block')

sns.boxplot(data=df, x='no_of_blocks', y='elapsed_time', ax=axs[1])
axs[1].set_yscale('log')
axs[1].set_title('Distribution of Elapsed Time by Number of Blocks')
axs[1].set_xlabel('Number of Blocks')
axs[1].set_ylabel('Elapsed Time (s)')

axs[1].get_legend().remove()

plt.savefig('subplot_matrix_multiplication.png', dpi=300, bbox_inches='tight')

df = pd.read_csv('../csv/matrix_tanspose.csv', sep=';', index_col=None)


fig, axs = plt.subplots(3, 1, figsize=(12, 20))
sns.set_theme(style="whitegrid")

sns.lineplot(data=df, x='n', y='elapsed_time', hue='block_size', marker='o')


# Filter data for type 'naive'
df_naive = df[df['type'] == 'naive']

# Filter data for type 'shared'
df_shared = df[df['type'] == 'shared']

sns.lineplot(data=df_naive, x='n', y='elapsed_time', hue='block_size', marker='o', ax=axs[0])

axs[0].set_xscale('log', base=2)
axs[0].set_yscale('log')
axs[0].set_title('Elapsed Time vs. Problem Size for Different Block Sizes and Types for naive type')
axs[0].set_xlabel('Problem Size (n)')
axs[0].set_ylabel('Elapsed Time (s)')
axs[0].legend(title='Block Size')

sns.lineplot(data=df_shared, x='n', y='elapsed_time', hue='block_size', marker='o', ax=axs[1])

axs[1].set_xscale('log', base=2)
axs[1].set_yscale('log')
axs[1].set_title('Elapsed Time vs. Problem Size for Different Block Sizes and Types for shared type')
axs[1].set_xlabel('Problem Size (n)')
axs[1].set_ylabel('Elapsed Time (s)')
axs[1].legend(title='Block Size')

sns.boxplot(data=df, x='type', y='elapsed_time', hue='block_size', ax=axs[2])
axs[2].set_yscale('log')
axs[2].set_title('Distribution of Elapsed Time by Type and Block Size')
axs[2].set_xlabel('Type')
axs[2].set_ylabel('Elapsed Time (s)')
axs[2].legend(title='Block Size')


axs[2].get_legend().remove()
# Show the plot
plt.savefig('subplot_matrix_transpose', dpi=300, bbox_inches='tight')
plt.show()