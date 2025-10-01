# Final Project – PPO Agent for CarRacing
## Objective

Train a PPO  agent to solve the CarRacing-v0 environment using visual input. The goal is to develop an agent that can complete laps efficiently using image-based reinforcement learning.

---

## Tasks Breakdown

These are just a way to go through the project. You need not follow these strictly.

### 1. Environment Setup

- Install dependencies: gym, Box2D, opencv-python, numpy, torch, stable-baselines3, etc.
- Launch CarRacing-v3 (v2 and lower versions are deprecated) and explore the observation and action spaces.

### 2.  Image Preprocessing + Frame Stacking

- Convert RGB frames to grayscale (or keep RGB)
- Resize to a smaller resolution (e.g., 84x84 or 96x96)
- Normalize pixel values
- Stack 3–4 frames to give the agent temporal context

### 3. PPO Agent Implementation

- Use Stable-Baselines3 or implement PPO from scratch. We expect you to implement PPO from scratch and compare its performance with that of existing models in the report.
- Start with `CnnPolicy` and make sure it works end-to-end. You can use other policies too.
- Configure hyperparameters: learning rate, entropy coef, batch size, etc.
- Once it's working, explore enhancements:
    - Custom CNN architecture
    - Recurrent PPO with LSTM
    - Reward shaping

### 4. Reward Shaping and Evaluation

- (Optional) Modify the reward function to penalize off-track behavior
- Save checkpoints at regular intervals
- Evaluate the agent on unseen tracks
- Record gameplay using `gym.wrappers.RecordVideo` or `imageio`

---

## Final Deliverables

### 1. Trained PPO Agent

- Submit the final checkpoint of your trained agent
- Aim to achieve an average reward of *≥900* across 10 episodes (this is a typical benchmark from literature). However, focus more on learning and experimentation than hitting an exact score.

### 2. Report (PDF or Markdown)

Your report should briefly describe:

- Preprocessing pipeline (frame size, stack, grayscale?)
- PPO architecture & hyperparameters
- Training process (reward graphs, episodes)
- Reward shaping (if used)
- Observations: challenges, interesting behaviours, overfitting, generalization

### 3. Demo Video or GIF

- Record a short clip of your trained agent completing a track (30–60 seconds)

Please structure your submission with:

- `code/` folder containing the implementation
- `report.pdf` or `report.md`
- `media/` folder for any images or videos
- Any other files/folder you find relevant
