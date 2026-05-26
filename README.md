# RL:Race and Learn - SoC 2025
## use requirements.txt file to download dependencies(pygame and others) to play the snake game from week 1 or to watch the snake agent in week 5 *Run everything else after week2 on Colab*


## Week 1

In Week 1, I learned Python OOP concepts and the basics of the Pygame library by building a classic Snake game. I represented the snake as a list of coordinates corresponding to its body segments and implemented movement using directional velocity variables updated through keyboard input.

I created core game functions for collision detection, score updates, and random food generation. The main game loop handled user input, snake movement, collision checks, rendering, and frame-rate control using Pygame’s clock module. The snake grows when food is collected, and the game ends if the snake collides with itself.

To improve the user experience, I also added start and end screens with interactive buttons, hover effects using mouse tracking, and a replay option that resets the game state.

## Week 2
In week 2, I learn about neural networks, CNNs and how to implement them in pytorch. For the weekly project, I decided to make a digit classifier using the MNIST dataset and pytorch with regular neural networks.      

I started by importing the required libraries. Since I used google colab to make this, I realised I could use a gpu that was available. Then, I initiated some variables I needed like pixels, size of each of my layers, digits, number of epochs, batch size and learning rate.       

After importing and loading the MNIST training and testing dataset, I defined a class NeuralNet as a child class of the neural network module in pytorch. Then, I made the object initialiser and forward pass functions in the class. I created an object and its loss and optimizer variables using nn.crossentropyloss and optim.SGD along with loss table and accuracy table lists which I used later to depict loss and accuracy as a function of epochs on training.      

Before I made the training loop, I measured the loss and accuracy before the training just to see the progress. Then, I trained my model using loss and optimizer and also monitored loss with each epoch. In each epoch, I also tested the model's accuracy by testing it against the MNIST testing dataset.       

In the end, I used matplotlib to plot the loss and accuracy subplots to show them as a function of epochs.

## Week 3
In Week 3, there was no assignment but still a lot to learn. The focus was on Markov Decision Processes (MDPs) and Deep RL. The lectures formalized how sequential decision-making problems can be structured using states, actions, and rewards. MDPs provided a clear mathematical framework, defining value functions and the Bellman equation as tools for evaluating and optimizing policies. Dynamic programming methods, like policy iteration and value iteration, demonstrated how optimal solutions can be computed when the environment’s dynamics are known.        
This week also introduced model-free methods and function approximation. The limitations of DP could be seen: real-world problems rarely have known transition models or tractable state spaces.

## Week 4
In Week 4, there was no assignment but still a lot to learn. I watched a lot of pytorch tutorials for reinforcement learning algorithms this week which helped me a lot- related to Q learning and DQN in particular.

## Week 5
Learning- dived deeper into DQN in Atari games and more.
Assignment- using Q learning to make the snake in the snake game an RL agent. This was particularly fun to implement as I watched the snake learn how to maneuver its way to the food.

## Week 6
Learnt PPO and how it outperforms older algorithms, like standard policy gradients, for example.
Read a lot of articles on stuff like openai gym and how to use environments and how to implement it on my own environment, etc.

## Week 7-8:
### Final Project
Here, I had to implement what I learnt in week 6 to make a car racing game in openai gym where the car is my agent. I trained the car using PPO to a decent degreee where it can find its way most of the time. Still, I think that if trained for about 10million timesteps, it would perform a lot better compared to the 1 million steps I used. However, I don't think it is feasible on my device or on colab because of the amount of time it takes to train even on a GPU.
