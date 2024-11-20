import sys
from typing import List, Tuple
from exceptions import TupleExistsError, OutOfBoundsError
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, MOUSEBUTTONDOWN
import pygame
import random

pygame.init()

direction = (1, 0)

screen_area = (500, 500)
play_area = (20, 20)
snake = [(5, 5), (4, 5), (3, 5)]
food = (10, 10)
eating: bool = False

screen = pygame.display.set_mode(screen_area)
pygame.display.set_caption("ИГРА ЗМЕЙКА  0_o")
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BUTTON_COLOR = (100, 200, 100)
BUTTON_HOVER_COLOR = (150, 250, 150)
BUTTON_TEXT_COLOR = (0, 0, 0)
turquoise = (0, 255, 204)
white = (255, 255, 255)
blue = (204, 255, 255)
width = heigth = 20
margin = 1

clock = pygame.time.Clock()
FPS = 10

font = pygame.font.Font(None, 40)

def field_rendering():
    for coloumn in range(play_area[0]):
        for row in range(play_area[1]):
            if (row + coloumn) % 2 == 0:
                color = blue
            else:
                color = white
            x = 40 + coloumn * width + margin * (coloumn + 1)
            y = 40 + row * heigth + margin * (row + 1)
            pygame.draw.rect(screen, color, (x, y, width, heigth))

def change_direction(direction, key):
    if key == K_UP and direction != (0, 1):
        return (0, -1)
    elif key == K_LEFT and direction != (1, 0):
        return (-1, 0)
    elif key == K_DOWN and direction != (0, -1):
        return (0, 1)
    elif key == K_RIGHT and direction != (-1, 0):
        return (1, 0)
    return direction

def draw_snake(snake):
    for segment in snake:
        col, row = segment
        x = 40 + col * (width + margin)
        y = 40 + row * (heigth + margin)
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, width, heigth))

def draw_food(food):
    col, row = food
    x = 40 + col * (width + margin)
    y = 40 + row * (heigth + margin)
    pygame.draw.rect(screen, FOOD_COLOR, (x, y, width, heigth))

def spawn_food(play_area: Tuple[int, int], snake: List[Tuple[int, int]]) -> Tuple[int, int]:
    while True:
        food_x = random.randint(0, play_area[0] - 1)
        food_y = random.randint(0, play_area[1] - 1)
        if (food_x, food_y) not in snake:
            return (food_x, food_y)

def draw_button(x, y, width, height, text, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, (x, y, width, height))
        if click[0] == 1 and action:
            action()
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, (x, y, width, height))

    text_surface = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def game_loop():
    global direction, eating, snake, food
    direction = (1, 0)
    snake = [(5, 5), (4, 5), (3, 5)]
    food = spawn_food(play_area, snake)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                direction = change_direction(direction, event.key)

        move_snake(snake, direction)
        if not is_within_bounds(snake[0], play_area):
            print("Game Over: Snake hit the wall!")
            return

        if snake[0] == food:
            eating = True
            food = spawn_food(play_area, snake)
        else:
            eating = False

        screen.fill(turquoise)
        field_rendering()
        draw_snake(snake)
        draw_food(food)
        pygame.display.update()
        clock.tick(FPS)

def main_menu():
    while True:
        screen.fill(turquoise)
        title = font.render("Змейка", True, BUTTON_TEXT_COLOR)
        screen.blit(title, (screen_area[0] // 2 - title.get_width() // 2, 50))

        draw_button(150, 200, 200, 50, "Старт", game_loop)
        draw_button(150, 300, 200, 50, "Выход", pygame.quit)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def move_snake(snake, direction):
    global eating
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.insert(0, new_head)
    if not eating:
        snake.pop()

def is_within_bounds(new_tuple: Tuple[int, int], play_area: Tuple[int, int]) -> bool:
    x, y = new_tuple
    width, height = play_area
    return 0 <= x < width and 0 <= y < height

main_menu()
