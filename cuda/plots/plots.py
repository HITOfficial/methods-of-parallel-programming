import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv('../csv/results.csv', sep=';')


# Set up the plot
fig, axs = plt.subplots(2, 1, figsize=(14, 10))
sns.set(style="whitegrid")

# Plot the data
sns.lineplot(data=df, x='n', y='elapsed_time', hue='threads_per_block', marker='o')

# Plot 1: Lineplot for threads_per_block
sns.lineplot(data=df, x='n', y='elapsed_time', hue='threads_per_block', marker='o', ax=axs[0])
axs[0].set_xscale('log', base=2)
axs[0].set_yscale('log')
axs[0].set_title('Elapsed Time vs. Problem Size for Different Threads Per Block')
axs[0].set_xlabel('Problem Size (n)')
axs[0].set_ylabel('Elapsed Time (s)')
axs[0].legend(title='Threads Per Block')




# Plot 4: Boxplot for no_of_blocks
sns.boxplot(data=df, x='no_of_blocks', y='elapsed_time', ax=axs[1])
axs[1].set_yscale('log')
axs[1].set_title('Distribution of Elapsed Time by Number of Blocks')
axs[1].set_xlabel('Number of Blocks')
axs[1].set_ylabel('Elapsed Time (s)')

axs[1].get_legend().remove()


# Show the plot
plt.savefig('subplot.png', dpi=300, bbox_inches='tight')
plt.show()