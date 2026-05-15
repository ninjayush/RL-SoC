import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 450
GRID_SIZE = 10
UI_HEIGHT = 50
FPS = 60
START_BUTTON_RECT = pygame.Rect(125, 195, 150, 60)
BTN_NORMAL = (32, 118, 173)
BTN_HOVER = (73, 170, 221)
BG_COLOR = (15, 20, 48)
BOARD_COLOR = (221, 232, 247)
SNAKE_COLOR = (235, 84, 65)
FOOD_COLOR = (106, 255, 158)
TEXT_COLOR = (20, 24, 40)
GRID_COLOR = (33, 44, 74)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

button_font = pygame.font.SysFont('Corbel', 34, bold=True)
score_font = pygame.font.SysFont('Corbel', 30)
label_font = pygame.font.SysFont('Corbel', 18)

# draw a button for start/restart screens
# hovered state gives better feedback to the user

def draw_button(text, rect, hovered):
    color = BTN_HOVER if hovered else BTN_NORMAL
    pygame.draw.rect(screen, color, rect, border_radius=12)
    label = button_font.render(text, True, (255, 255, 255))
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)


def wait_for_button_click(label_text):
    while True:
        mouse_pos = pygame.mouse.get_pos()
        hovered = START_BUTTON_RECT.collidepoint(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and hovered:
                return

        screen.fill(BG_COLOR)
        draw_button(label_text, START_BUTTON_RECT, hovered)
        pygame.display.flip()
        clock.tick(FPS)


def draw_score(score):
    board_rect = pygame.Rect(0, 0, SCREEN_WIDTH, UI_HEIGHT)
    pygame.draw.rect(screen, BOARD_COLOR, board_rect)
    pygame.draw.line(screen, GRID_COLOR, (0, UI_HEIGHT), (SCREEN_WIDTH, UI_HEIGHT), 2)
    score_label = score_font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_label, (16, 10))
    hint_label = label_font.render("Use arrow keys or WASD", True, TEXT_COLOR)
    screen.blit(hint_label, (SCREEN_WIDTH - hint_label.get_width() - 16, 17))


def random_food_position(snake_positions):
    occupied = set(snake_positions)
    while True:
        x = random.randrange(0, SCREEN_WIDTH // GRID_SIZE) * GRID_SIZE
        y = random.randrange(UI_HEIGHT // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE) * GRID_SIZE
        if (x, y) not in occupied:
            return x, y


def wrap_position(x, y):
    x = x % SCREEN_WIDTH
    y = UI_HEIGHT + ((y - UI_HEIGHT) % (SCREEN_HEIGHT - UI_HEIGHT))
    return x, y


def reset_snake():
    start_x = 200
    start_y = 200
    return [
        (start_x, start_y),
        (start_x - GRID_SIZE, start_y),
        (start_x - 2 * GRID_SIZE, start_y),
        (start_x - 3 * GRID_SIZE, start_y),
        (start_x - 4 * GRID_SIZE, start_y),
    ]


def draw_game(snake, food, score):
    screen.fill(BG_COLOR)
    draw_score(score)
    pygame.draw.rect(screen, GRID_COLOR, (0, UI_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - UI_HEIGHT), 2, border_radius=12)
    pygame.draw.circle(screen, FOOD_COLOR, (food[0] + GRID_SIZE // 2, food[1] + GRID_SIZE // 2), GRID_SIZE // 2)
    # draw the snake as square segments, not joined circles
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))
    pygame.display.flip()


def game_loop():
    snake = reset_snake()
    direction = (1, 0)
    next_direction = direction
    food = random_food_position(snake)
    score = 0
    move_delay = 120
    timer = 0

    while True:
        dt = clock.tick(FPS)
        timer += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # use WASD or arrow keys, but disallow reversing direction
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP) and direction != (0, 1):
                    next_direction = (0, -1)
                elif event.key in (pygame.K_s, pygame.K_DOWN) and direction != (0, -1):
                    next_direction = (0, 1)
                elif event.key in (pygame.K_a, pygame.K_LEFT) and direction != (1, 0):
                    next_direction = (-1, 0)
                elif event.key in (pygame.K_d, pygame.K_RIGHT) and direction != (-1, 0):
                    next_direction = (1, 0)

        if timer >= move_delay:
            timer -= move_delay
            direction = next_direction
            head_x, head_y = snake[0]
            head_x += direction[0] * GRID_SIZE
            head_y += direction[1] * GRID_SIZE
            head_x, head_y = wrap_position(head_x, head_y)
            new_head = (head_x, head_y)

            snake.insert(0, new_head)

            if new_head == food:
                score += 10
                food = random_food_position(snake)
                move_delay = max(60, move_delay - 1)
            else:
                snake.pop()

            if new_head in snake[1:]:
                break

        draw_game(snake, food, score)

    wait_for_button_click("RESTART")


def main():
    wait_for_button_click("START")
    while True:
        game_loop()


if __name__ == "__main__":
    main()
