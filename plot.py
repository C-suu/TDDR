# This script reproduces Figure 2 (b) from the TDDR paper, visualizing the performance in HalfCheetah across five random seeds. This pipeline is generally applicable to other baselines and environments: simply execute the respective algorithms across the desired environments to reproduce Figures 2, 3, and 4 from the paper.

import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

n_smooth = 5
n_range = 5

environments = ['HalfCheetah']

for environment in environments:

    all_data = {'TDDR': []}

    # Directory path
    # Update this path to your local data directory; no further modifications are required.
    folder_path = r'.\HalfCheetah'

    def smooth_curve(data, smoothing_window=n_smooth):
        smoothed_data = []
        for i in range(len(data)):
            start = max(0, i - smoothing_window)
            end = min(len(data), i + smoothing_window + 1)
            smoothed_data.append(np.mean(data[start:end]))
        return smoothed_data

    genshin_impact_colors = [(208, 119, 151)]
       
    # Normalize RGB values to the [0, 1] range
    genshin_impact_colors = [(r/255., g/255., b/255.) for r, g, b in genshin_impact_colors]

    sns.set_theme(style="darkgrid")
    sns.set_palette(genshin_impact_colors)

    plt.figure(figsize=(10, 6))

    # Load empirical data across the 5 independent seeds
    for j in range(1, n_range + 1): 
        file_path = os.path.join(folder_path, f'TDDR_{environment}-v2_{j}_avg_rewards.npy')
        print(f"Loading: {file_path}")
        data = np.load(file_path)
        all_data['TDDR'].append(data)

    # Compute the mean and standard deviation
    data_array = np.array(all_data['TDDR'])
    avg_reward = np.mean(data_array, axis=0)
    std_dev = np.std(data_array, axis=0)

    # Apply curve smoothing
    smoothed_reward = smooth_curve(avg_reward, smoothing_window=n_smooth)
    smoothed_std_dev = smooth_curve(std_dev, smoothing_window=n_smooth)

    smoothed_reward = np.array(smoothed_reward)
    smoothed_std_dev = np.array(smoothed_std_dev)

    # Plot the shaded region
    plt.fill_between(range(len(smoothed_reward)), smoothed_reward - smoothed_std_dev,
                    smoothed_reward + smoothed_std_dev, alpha=0.15)
    
    # Plot the learning curve
    plt.plot(smoothed_reward, label='TDDR', linewidth=2)

    plt.xlabel('Million Steps', fontsize='xx-large')
    plt.ylabel('Return', fontsize='xx-large')
    plt.xticks(np.linspace(0, 201, num=6), ['0', '0.2', '0.4', '0.6', '0.8', '1.0'], fontsize='xx-large')
    plt.yticks(fontsize='xx-large')
    plt.legend(fontsize='xx-large', loc='lower right', ncol=2)
    plt.title(f'{environment}', fontsize='xx-large')

plt.tight_layout()

plt.show()

