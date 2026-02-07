# 这是TDDR论文的图2的子图b，是HalfCheetah运行五次的画图程序。其他环境和其他算法同理，只需要运行不同算法和不同环境，即可画出TDDR的图2，3，4。

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

    # 文件夹路径
    # 将这个路径替换为数据文件所在的路径，其余不需要修改
    folder_path = r'C:\Users\123\Desktop\新建文件夹\HalfCheetah'

    # 平滑处理函数
    def smooth_curve(data, smoothing_window=n_smooth):
        smoothed_data = []
        for i in range(len(data)):
            start = max(0, i - smoothing_window)
            end = min(len(data), i + smoothing_window + 1)
            smoothed_data.append(np.mean(data[start:end]))
        return smoothed_data

    genshin_impact_colors = [(208, 119, 151)]
       
    # 将 RGB 值转换为 [0, 1] 范围内的值
    genshin_impact_colors = [(r/255., g/255., b/255.) for r, g, b in genshin_impact_colors]

    sns.set_theme(style="darkgrid")
    sns.set_palette(genshin_impact_colors)

    plt.figure(figsize=(10, 6))

    # 读取 5 个种子的数据
    for j in range(1, n_range + 1): 
        file_path = os.path.join(folder_path, f'TDDR_{environment}-v2_{j}_avg_rewards.npy')
        print(f"正在读取: {file_path}")
        data = np.load(file_path)
        all_data['TDDR'].append(data)

    # 计算平均值和标准差
    data_array = np.array(all_data['TDDR'])
    avg_reward = np.mean(data_array, axis=0)
    std_dev = np.std(data_array, axis=0)

    # 平滑处理
    smoothed_reward = smooth_curve(avg_reward, smoothing_window=n_smooth)
    smoothed_std_dev = smooth_curve(std_dev, smoothing_window=n_smooth)

    smoothed_reward = np.array(smoothed_reward)
    smoothed_std_dev = np.array(smoothed_std_dev)

    # 绘制阴影区域
    plt.fill_between(range(len(smoothed_reward)), smoothed_reward - smoothed_std_dev,
                    smoothed_reward + smoothed_std_dev, alpha=0.15)
    
    # 绘制曲线
    plt.plot(smoothed_reward, label='TDDR', linewidth=2)

    plt.xlabel('Million Steps', fontsize='xx-large')
    plt.ylabel('Return', fontsize='xx-large')
    plt.xticks(np.linspace(0, 201, num=6), ['0', '0.2', '0.4', '0.6', '0.8', '1.0'], fontsize='xx-large')
    plt.yticks(fontsize='xx-large')
    plt.legend(fontsize='xx-large', loc='lower right', ncol=2)
    plt.title(f'{environment}', fontsize='xx-large')

plt.tight_layout()

plt.show()
