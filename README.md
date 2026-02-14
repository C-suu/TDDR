# Double Actor-Critic with TD Error-Driven Regularization in Reinforcement Learning
Torch implementation of the TDDR algorithm.

# Citation
If you find our work helpful, please consider cite our work.

```bibtex
@article{chen2025doubleactorcritic,
  author  = {Haohui Chen and Zhiyong Chen and Aoxiang Liu and Wentuo Fang},
  title   = {Double Actor-Critic with TD Error-Driven Regularization in Reinforcement Learning},
  journal = {Neural Networks},
  year    = {2025},
  doi     = {https://doi.org/10.1016/j.neunet.2025.108323}
}
```

## We evaluated TDDR in HalfCheetah across five random seeds. The evaluation metrics were logged as `.npy` files, and the corresponding learning curves were generated using the `plot.py` script. The empirical results are presented below:
<img width="2000" height="1200" alt="b0442bf7c3d8533eb19ebaedff808c26" src="https://github.com/user-attachments/assets/cab32c89-460d-4bde-aed2-864140a60072" />


# Code for comparison algorithms:

Actor-critic:

DDPG and TD3: https://github.com/sfujim/TD3.git

SAC: https://github.com/quantumiracle/Popular-RL-Algorithms.git or https://github.com/vwxyzjn/cleanrl.git

PPO: https://github.com/vwxyzjn/cleanrl.git

Double actor-critic:

DARC: https://github.com/dmksjfl/DARC.git

SD3: https://github.com/ling-pan/SD3.git

GD3: https://github.com/dmksjfl/GD3.git

State-of-the-art:

TD7: https://github.com/sfujim/TD7.git

TD3-N: https://github.com/MiaomiaoZhang97/Multi-steps.git

AC-Off-POC-TD3: https://github.com/baturaysaglam/AC-Off-POC.git

DSACv2: https://github.com/Jingliang-Duan/DSAC-v2.git

AC-TD3: https://github.com/Jiang-HB/AC_CDQ.git

DivAC: https://github.com/yzyvl/DivAC.git


