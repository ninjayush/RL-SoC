# RL CarRacing-v3 PPO Project Report
Preprocessing Pipeline contains:
Frame size- 84×84 pixels (downsampled from original)
Frame stack- 4 consecutive grayscale frames (for temporal context)
Grayscale- all images converted to grayscale using OpenCV before stacking
Observation shape- (4, 84, 84); channel-first order, type uint8 (letting SB3 CnnPolicy handle normalization internally)

Environment wrappers used:
RecordEpisodeStatistics (for logging episode rewards/lengths)
(No reward shaping or normalization applied; frames are stored as stack of 4 in channel dimension.)

PPO Architecture:
Policy network- Stable-Baselines3 "CnnPolicy" (NatureCNN-style 3-layer ConvNet)
RL Algorithm- Proximal Policy Optimization (PPO)

Hyperparameters:
Learning rate- 0.0003 (default)
n_steps- default (2,048 per update)
Discount factor gamma- default (0.99)
Batch size- default (64)
Frame stacking- 4
Checkpointing- Models saved every 100,000 steps
Training steps- Up to 1 million timesteps per run

Training Process:
Ran on Google Colab using GPU (cuda).

TensorBoard and SB3 logs tracked:
rollout/ep_rew_mean: the main learning signal (mean episode reward)
rollout/ep_len_mean, losses, explained variance, etc.

Reward curve summary:
ep_rew_mean rose from random (near 0–100) to typically between 200–360 after 500k–800k steps yet oscillated a little bit.

Episode length consistently close to 1,000 frames (full episodes).
Longer training or major hyperparameter tuning not yet performed.

No Reward Shaping used
-default CarRacing-v3 rewards; no added shaping, normalization, or modification.

Frame stacking is the only form of temporal shaping used (standard for visual RL).

Observations and Challenges
Training progress plateaus at ~250–350 mean reward — agent does not reach “expert” driving (~700–900 reward); overfitting not observed, but no generalization to higher scores.
It also takes hours to train.

Reward curve is noisy, showing learning but with considerable variability, performance can drop and recover as seen in logs.

High clip_fraction/entropy_loss and variable value_loss in logs reflect PPO's struggle with the sparse, difficult CarRacing-v3 reward dynamics.

Colab timeouts/interruptions require frequent checkpointing and careful syncing with Google Drive.

Interesting Behaviors
Agent quickly learns not to quit instantly, tracks increase in lap time.
Plateaued agents can survive but still have trouble making sharp turns or recovering from skids.

Some evaluations: agent spins or gets stuck despite apparent learning progress.

To reach higher performance, it would probably take more timesteps and maybe more exploration based algorithm.