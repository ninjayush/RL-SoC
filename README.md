# RL:Race and Learn - SoC 2025

## Week 1

In week 1, I had to learn about python classes/OOP and pygame and make a standard snake game from pygame.       
After learning from the resources provided by my mentors, I started writing the code for the game.      

First, I created the snake —a list of lists that contained the coordinates of the snake's body parts' (rectangles) positions by assigning it an initial position.     

Then, I chose a background colour and set the score to 0. I also chose certain attributes of the snake that I thought were necessary- velocity, maximum velocity, velocity in x, velocity in y, velocity in x and y boolean, collision boolean,  and iterator i for a while loop.        

Here, velocity in x and y were just used to store 0 and 1, which I used for multiplication later. Velocity in x and y boolean were also the same, just boolean. I could have used just 1 variable instead of these 4, but using these made writing the code easier for me.       

After this, I defined 3 crucial functions which were to be used in the game loop: scoreboard update- to add to the score variable if there was a collision (snake reached the ball), ball generator- generated a new ball after a collision, collision checker- to return whether a collision had happened.      

Now, the game loop. At the start of the game loop, I used pygame.events.get to check for the keys pressed, assuming the player is using wasd or arrow keys. According to this, I assigned the boolean and numerical velocities in the x and y direction.

Then, I captured the coordinates of the snake's head in that specific frame. The reason for this was to keep the snake moving, I had to change the coordinates of its head and remove its tail every frame to keep the length constant unless it had a collision- in that case, the tail isn't removed and the snake grows in length.     

Here I also called the aforementioned functions in a logical order so the execution doesn't get messed up. I also used the clock object from the pygame time module to make the game 60fps. To stop discontinuity, I drew the snake in every frame with its updated coordinates. If the snake collides with its own body parts, the game ends.     

After I was done with the game mechanics, I decided to make a start and end screen(with a replay option) with buttons. I used mouse tracking coordinates to check for cursor hovering- to get a blinker sort of feel in the buttons. When the start button was clicked, the game started. When the restart button was clicked, in the game loop, I restored the initial conditions and continued to the next iteration in the loop.

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
