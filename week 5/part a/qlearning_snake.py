import pygame
import numpy as np
import random
import pickle #to save the qtable as a binary file
import matplotlib.pyplot as plt
from collections import deque

# this snake loves crashing into itself

GRID_SIZE = 20  
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 450

BG_COLOR = (0, 128, 0)  
SNAKE_COLOR = (52, 21, 57)  
FOOD_COLOR = (255, 0, 0)  
SCOREBOARD_COLOR = (0, 0, 0)  
GRID_LINE_COLOR = (50, 50, 50)  


# Q-Learning parameters
LEARNING_RATE = 0.01
DISCOUNT = 0.95
EPISODES = 25000
SHOW_EVERY = 500
epsilon = 0.9 #high exploration
epsilon_decay = 0.95

# Q-table setup
# State representation: (food_dx, food_dy, danger_left, danger_front, danger_right, current_direction)
# Actions: 0=left, 1=forward, 2=right

Q_table = np.random.uniform(low=-1, high=1, size=(3,3,2,2,2,4,3)) # Random initialization

episode_scores = []
moving_avg_scores = []
score_window = deque(maxlen=100)

class SnakeGameAI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Q-Learning Snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 20)
        
        self.reset_game()


    def draw_game(self, screen, snake, food, score):
        screen.fill(BG_COLOR)
        
        # Scoreboard
        pygame.draw.rect(screen, SCOREBOARD_COLOR, (0, 0, SCREEN_WIDTH, 50))
        pygame.draw.line(screen, (0, 0, 0), (0, 50), (SCREEN_WIDTH, 50), 2)
        
        # Score text
        font = pygame.font.SysFont('freesanbold.ttf', 40)
        text = font.render(f"Score: {score}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, 25))
        screen.blit(text, text_rect)
        
        # Grid
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, GRID_LINE_COLOR, (x, 50), (x, SCREEN_HEIGHT))
        for y in range(50, SCREEN_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, GRID_LINE_COLOR, (0, y), (SCREEN_WIDTH, y))
        
        # Snake
        for segment in snake:
            rect = pygame.Rect(segment[0]*GRID_SIZE, segment[1]*GRID_SIZE + 50, 
                            GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, SNAKE_COLOR, rect, 0) 
        
        # Food
        food_rect = pygame.Rect(food[0]*GRID_SIZE, food[1]*GRID_SIZE + 50, 
                            GRID_SIZE, GRID_SIZE)
        pygame.draw.circle(screen, FOOD_COLOR, food_rect.center, 10)
        
        pygame.display.update()


    def get_state(self, snake, food, direction):
        head = snake[0]
        
        # Food relative position
        food_dx = np.sign(food[0] - head[0])
        food_dy = np.sign(food[1] - head[1])
        
        
        # Danger detection
        directions = {
            'left': (-1, 0) if direction == (0, -1) else 
                    (1, 0) if direction == (0, 1) else 
                    (0, 1) if direction == (1, 0) else 
                    (0, -1),
            'forward': direction,
            'right': (1, 0) if direction == (0, -1) else 
                    (-1, 0) if direction == (0, 1) else 
                    (0, -1) if direction == (1, 0) else 
                    (0, 1)
        }
        
        dangers = []

        for d in ['left', 'forward', 'right']:
            new_pos = (head[0] + directions[d][0], head[1] + directions[d][1])
            # Check boundaries
            if (new_pos[0] < 0 or new_pos[0] >= GRID_SIZE or 
                new_pos[1] < 0 or new_pos[1] >= GRID_SIZE or 
                new_pos in snake):
                dangers.append(1)
            else:
                dangers.append(0)
        
        # Current direction
        if direction == (1, 0): dir_idx = 0    # right
        elif direction == (-1, 0): dir_idx = 1 # left
        elif direction == (0, 1): dir_idx = 2  # down
        else: dir_idx = 3                       # up
        
        state = (
            food_dx, food_dy,  # Food direction
            dangers[0], dangers[1], dangers[2],  # Danger left, front, right
            dir_idx  # Current direction
        )
        
        return state


    def get_action(self, state):
        if random.random() < epsilon:
            return random.randint(0, 2)
        
        else:
            return np.argmax(Q_table[state])
        # else:
        #     if state in q_table:
        #         return np.argmax(q_table[state])
        #     else:
        #         return random.randint(0, 2)


    def update_q_table(self, state, action, reward, new_state):
    
        # Q-learning formula
        max_future_q = np.max(Q_table[new_state])
        current_q = Q_table[state][action]
        
        new_q = (1-LEARNING_RATE)*current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q) #Bellman
        Q_table[state][action] = new_q


    def get_direction_from_action(self, action, current_direction):
        # Action: 0=left, 1=forward, 2=right
        if current_direction == (1, 0):  
            if action == 0: return (0, -1)  
            elif action == 1: return (1, 0)  
            elif action == 2: return (0, 1)  
        elif current_direction == (-1, 0): 
            if action == 0: return (0, 1)  
            elif action == 1: return (-1, 0) 
            elif action == 2: return (0, -1)  
        elif current_direction == (0, 1):  
            if action == 0: return (1, 0) 
            elif action == 1: return (0, 1) 
            elif action == 2: return (-1, 0)  
        elif current_direction == (0, -1):  
            if action == 0: return (-1, 0) 
            elif action == 1: return (0, -1)  
            elif action == 2: return (1, 0)  
        return current_direction


    def reset_game(self):
        snake = [[10, 10], [9, 10], [8, 10]]
        food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
        while food in snake:
            food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
        
        direction = (1, 0)
        score = 0
        steps = 0
        done = False
        return snake, food, direction, score, steps, done


    def train_ai(self):
        global epsilon, k
        
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Q-Learning Snake")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Arial', 20)
        
        for episode in range(EPISODES):
            # Reset game state
            snake, food, direction, score, steps, done = self.reset_game()
            
            state = self.get_state(snake, food, direction)
            
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                
                action = self.get_action(state)
                new_direction = self.get_direction_from_action(action, direction)
                
                head = snake[0]
                new_head = [(head[0] + new_direction[0]) % GRID_SIZE, 
                        (head[1] + new_direction[1]) % GRID_SIZE]
                
                # Check for collisions
                if new_head in snake:
                    reward = -300
                    done = True
                else:
                    snake.insert(0, new_head)
                    
                    if new_head == food:
                        reward = 10
                        score += 10
                        food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
                        while food in snake:
                            food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
                    else:
                        reward = -1  
                        snake.pop()
                    
                    # Check if stuck (too many steps without eating)
                    steps += 1
                    if steps > 100 * len(snake):
                        reward = -50
                        done = True
                
                new_state = self.get_state(snake, food, new_direction)
                
                self.update_q_table(state, action, reward, new_state)
                
                state = new_state
                direction = new_direction
                
                if episode % SHOW_EVERY == 0:
                    self.draw_game(screen, snake, food, score)
                    clock.tick(60)
            
            episode_scores.append(score)
            score_window.append(score)
            
            if len(score_window) == 100:
                moving_avg_scores.append(np.mean(score_window))


            #Epsilon reduction
            if episode%500 == 0 and episode > 0:
                epsilon = max(0.1, epsilon * epsilon_decay)  # Avoid going below 0.1
            
            #Print progress
            if episode % 100 == 0:
                print(f"Episode: {episode}, Score: {score}, Epsilon: {epsilon:.2f}")
        
        #Save Q-table in a binary file
        with open('qtable.pickle', 'wb') as f:
            pickle.dump(Q_table, f)
        
        pygame.quit()

        
        plt.figure(figsize=(10,5))
        plt.plot(episode_scores, alpha=0.3, label='Individual Scores')
        if moving_avg_scores:
            plt.plot(range(99, 99+len(moving_avg_scores)), moving_avg_scores, 'r-', label='100-episode Avg')
        plt.title('Training Progress')
        plt.xlabel('Episode')
        plt.ylabel('Score')
        plt.legend()
        plt.grid()
        plt.savefig('training_results.png')
        plt.show()


    def play_with_ai(self):
    
        try:
            with open('qtable.pickle', 'rb') as f:
                loaded_q_table = pickle.load(f)
        except:
            print("No Q-table found. Train the AI first.")
            return
        
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("AI Snake")
        clock = pygame.time.Clock()
        font = pygame.font.SysFont('Arial', 20)
        
        snake = [[10, 10], [9, 10], [8, 10]]
        food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
        while food in snake:
            food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
        
        direction = (1, 0)
        score = 0
        done = False
        
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            state = self.get_state(snake, food, direction)
            if state in loaded_q_table:
                action = np.argmax(loaded_q_table[state])
            else:
                action = random.randint(0, 2)
            
            new_direction = self.get_direction_from_action(action, direction)
            
            head = snake[0]
            new_head = [(head[0] + new_direction[0]) % GRID_SIZE, 
                    (head[1] + new_direction[1]) % GRID_SIZE]
            
            if new_head in snake:
                done = True
            else:
                snake.insert(0, new_head)
                
                if new_head == food:
                    score += 10
                    food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
                    while food in snake:
                        food = [random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)]
                else:
                    snake.pop()
            
            direction = new_direction
            
            screen.fill((0, 128, 0))
            
            for x in range(0, SCREEN_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, (50, 50, 50), (x, 50), (x, SCREEN_HEIGHT))
            for y in range(50, SCREEN_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))
            
            for segment in snake:
                rect = pygame.Rect(segment[0]*GRID_SIZE, segment[1]*GRID_SIZE + 50, 
                                GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(screen, (52, 21, 57), rect, 0, 3)
            
            food_rect = pygame.Rect(food[0]*GRID_SIZE, food[1]*GRID_SIZE + 50, 
                                GRID_SIZE, GRID_SIZE)
            pygame.draw.circle(screen, (255, 0, 0), food_rect.center, 10)
            
            score_text = f"Score: {score}"
            text_surface = font.render(score_text, True, (255, 255, 255))
            screen.blit(text_surface, (10, 10))
            
            pygame.display.update()
            clock.tick(10)  # Slower speed for viewing
        
        pygame.quit()



print("1. Train AI")
print("2. Watch AI play")
choice = input("Enter choice (1/2): ")

snake= SnakeGameAI()

if choice == "1":
    snake.train_ai()
elif choice == "2":
    snake.play_with_ai()
else:
    print("Invalid choice")