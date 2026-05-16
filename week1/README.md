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