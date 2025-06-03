import pygame
import sys
import random

pygame.init()

start_screen = pygame.display.set_mode((400, 450))

pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


box_topleft = (125, 195)
box_dimensions = (150, 60)

startfont = pygame.font.SysFont('Corbel',40)
endfont = pygame.font.SysFont('Corbel',30)
starttext = startfont.render('START' , True , (255, 255, 255))
endtext = endfont.render('RESTART' , True , (255, 255, 255))

BTN_NORMAL = (0, 100, 180)       # Deep blue
BTN_HOVER = (0, 180, 255)        # Bright blue

start=False

while not start:
    
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if ev.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if box_topleft[0] <= mouse[0] <= box_topleft[0]+box_dimensions[0] and box_topleft[1] <= mouse[1] <= box_topleft[1]+box_dimensions[1]:
                start = True
    
    mouse = pygame.mouse.get_pos()

    start_screen.fill((0,0,0))
    
    if box_topleft[0] <= mouse[0] <= box_topleft[0]+box_dimensions[0] and box_topleft[1] <= mouse[1] <= box_topleft[1]+box_dimensions[1]:
        pygame.draw.rect(start_screen, BTN_HOVER, [box_topleft[0], box_topleft[1], box_dimensions[0], box_dimensions[1]])
        
    else:
        pygame.draw.rect(start_screen, BTN_NORMAL, [box_topleft[0], box_topleft[1], box_dimensions[0], box_dimensions[1]])


    start_screen.blit(starttext , (box_topleft[0]+20, box_topleft[1]+10))
    pygame.display.update()


    clock.tick(60)
    



bg= (15, 15, 35) 

#snake coordinates
snake= [[200, 200, 10, 10], [190, 200, 10, 10], [180, 200, 10, 10], [170, 200, 10, 10], [160, 200, 10, 10]]

screen = pygame.display.set_mode((400, 450))

screen.fill(bg)

score = 0

font = pygame.font.SysFont('freesanbold.ttf', 10)


velocity = 80/60   
max_velocity = 360/60
vel_x_bool = True
vel_x = 1
vel_y = 0
vel_y_bool = False
counter = 0
i=0
collision = False

def scoreboard_update(score, collision):
    if collision:
        score += 10
    font = pygame.font.SysFont('freesanbold.ttf', 40)
    text = font.render(f'Score: {score}', True, (0, 0, 0))
    text_Rect = text.get_rect()
    text_Rect.center = (200, 25)
    backg=pygame.Rect(0, 0, 400, 50)
    pygame.draw.rect(screen, (173, 216, 230), backg)
    pygame.draw.line(screen, (0, 0, 0), (0, 50), (400, 50), 2)  # Draw a line at the bottom of the scoreboard
    screen.blit(text, text_Rect)
    return score


def ball_generator():
    while True:
        p = random.randint(0, 39) * 10
        q = random.randint(5, 44) * 10
        overlap = False
        for segment in snake:
            if abs(segment[0] - p) < 10 and abs(segment[1] - q) < 10:
                overlap = True
                break
        if not overlap:
            return [p, q]



def collision_check(snake, ball):
    # Check if the snake's head overlaps with the ball (allowing for a small area)
    snake_x = int(snake[0][0])
    snake_y = int(snake[0][1])
    ball_x = int(ball[0])
    ball_y = int(ball[1])
    if abs(snake_x - ball_x) < 10 and abs(snake_y - ball_y) < 10:
        return True
    return False

ball=[400,400]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                # ("Move the character forwards")
                if vel_x_bool:
                    vel_x_bool = False
                    vel_y_bool = True
                    vel_y = -1
                    vel_x = 0



                
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                #("Move the character backwards")
                if vel_x_bool:
                    vel_x_bool = False
                    vel_y_bool = True
                    vel_y = 1
                    vel_x = 0


            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                #("Move the character left")
                if vel_y_bool:
                    vel_x_bool = True
                    vel_y_bool = False
                    vel_y = 0
                    vel_x = -1


            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                #("Move the character right")
                if vel_y_bool:
                    vel_x_bool = True
                    vel_y_bool = False
                    vel_y = 0
                    vel_x = 1



    

    #frame counter and velocity increment
    i+=1
    if i == counter + 60:
        velocity += 160/3600
        counter = i
        if velocity > max_velocity:
            velocity = max_velocity

    

    #snake elongation and coordinate update
    new_snakex = snake[0][0]
    new_snakey = snake[0][1]
    if vel_x_bool:
        new_snakex = snake[0][0] + velocity * vel_x
        if new_snakex > 400:
            new_snakex = 0
        elif new_snakex < 0:
            new_snakex = 400
    else:
        new_snakey = snake[0][1] + velocity * vel_y
        if new_snakey > 450:
            new_snakey = 50
        elif new_snakey < 50: 
            new_snakey = 450

    
    snake.insert(0, [new_snakex, new_snakey, 10, 10])

    if i==1:
        pass
    else:
        collision = collision_check(snake, ball)

    if not collision:
        snake.pop()

    if i==1 or collision:
        ball = ball_generator()

    pygame.draw.circle(screen, (0, 0, 255), ball, 5)

    score = scoreboard_update(score, collision)


    
    # Draw the snake
    for j in snake:
        pygame.draw.rect(screen, (220, 20, 60), j, 0, 3)

    # Update the display
    pygame.display.update()
    
    # Control the frame rate
    clock.tick(60)

    # Move the snake

   
    screen.fill(bg)  # Clear the screen before drawing the snake again

    #self collision check
    if snake[0][0] in [segment[0] for segment in snake[1:]] and snake[0][1] in [segment[1] for segment in snake[1:]]:
        # Make self-collision more liberal: allow a small overlap area (less strict)
        for segment in snake[1:]:
            if abs(snake[0][0] - segment[0]) < 4 and abs(snake[0][1] - segment[1]) < 4:
    
                end= False
                '''#implement restart button and screen here'''
                # Ensure the restart button is drawn and displayed before entering the loop
                start_screen.fill((0,0,0))
                pygame.draw.rect(start_screen, BTN_NORMAL, [box_topleft[0], box_topleft[1], box_dimensions[0], box_dimensions[1]])
                start_screen.blit(endtext , (box_topleft[0]+20, box_topleft[1]+10))
                pygame.display.update()

                while not end:
    
                    for ev in pygame.event.get():
                        
                        if ev.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            
                        if ev.type == pygame.MOUSEBUTTONDOWN:
                            mouse = pygame.mouse.get_pos()
                            if box_topleft[0] <= mouse[0] <= box_topleft[0]+box_dimensions[0] and box_topleft[1] <= mouse[1] <= box_topleft[1]+box_dimensions[1]:
                                end = True
                                break


                    
                    mouse = pygame.mouse.get_pos()

                    start_screen.fill((0,0,0))
                    
                    if box_topleft[0] <= mouse[0] <= box_topleft[0]+box_dimensions[0] and box_topleft[1] <= mouse[1] <= box_topleft[1]+box_dimensions[1]:
                        pygame.draw.rect(start_screen, BTN_HOVER, [box_topleft[0], box_topleft[1], box_dimensions[0], box_dimensions[1]])
                        
                    else:
                        pygame.draw.rect(start_screen, BTN_NORMAL, [box_topleft[0], box_topleft[1], box_dimensions[0], box_dimensions[1]])


                    start_screen.blit(endtext , (box_topleft[0]+20, box_topleft[1]+10))
                    pygame.display.update()


                    clock.tick(60)

        score= 0
        snake = [[200, 200, 10, 10], [190, 200, 10, 10], [180, 200, 10, 10], [170, 200, 10, 10], [160, 200, 10, 10]]
        velocity = 80/60
        vel_x_bool = True          
        vel_x = 1
        vel_y = 0
        vel_y_bool = False
        counter = 0
        i = 0
        collision = False
        ball = [400, 400]
        continue
                


