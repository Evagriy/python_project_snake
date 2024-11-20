import sys
from typing import List, Tuple
from exceptions import TupleExistsError, OutOfBoundsError
from pygame.locals import KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT
import pygame
import main
import random

pygame.init()

direction = (1, 0)

screen_area = (500, 500)
play_area = (20, 20)
snake = [(5, 5), (4, 5), (3, 5)]
food = (10, 10)
eating:  bool = False

screen = pygame.display.set_mode(screen_area)
pygame.display.set_caption("ИГРА ЗМЕЙКА  0_o")
jpg = pygame.image.load("snake.jpg")
pygame.display.set_icon(jpg)
screen.fill((255, 255, 255))

SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
turquoise = (0, 255, 204)
white = (255, 255, 255)
blue = (204, 255, 255)
width = heigth = 20
margin = 1

clock = pygame.time.Clock()
FPS = 10

def field_rendering():
    for coloumn in range(play_area[0]):
        for row in range(play_area[1]):
            if (row + coloumn) % 2 == 0:
                color = blue
            else:
                color = white
            x = 40 + coloumn * width + margin * (coloumn + 1)
            y = 40 + row * heigth + margin * (row + 1)
            pygame.draw.rect(screen, color,(x, y, width, heigth))

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


def check_tuple(list_numbers: List[tuple[int, int]], new_tuple: Tuple[int, int]) -> bool:
    if new_tuple in list_numbers:
        raise TupleExistsError("game over")

def is_within_bounds(new_tuple: Tuple[int, int], play_area: Tuple[int, int]) -> bool:
    x, y = new_tuple
    width, height = play_area
    return 0 <= x < width and 0 <= y < height


def add_tuple(list_numbers: List[Tuple[int, int]], new_tuple: Tuple[int, int], eating: bool, play_area: Tuple[int, int]) -> None:
    if not is_within_bounds(new_tuple, play_area):
        raise OutOfBoundsError(f"Tuple {new_tuple} is out of bounds for play area {play_area}")

    try:
        check_tuple(list_numbers, new_tuple)
        list_numbers.append(new_tuple)
        print(f"tuple {new_tuple} add in list.")
    except TupleExistsError as e:
        print(e)
        return

    if eating:
        print("Похавал.")
    elif eating == False:
        del list_numbers[0]
        print("Голодуха")

    print(list_numbers)

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])  # Новая позиция головы
    snake.insert(0, new_head)  # Добавляем новую голову
    if not eating:
        snake.pop()  # Удаляем последний элемент, если не еда

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == KEYDOWN:
            direction = change_direction(direction, event.key)
            print(f"New direction: {direction}")

    move_snake(snake, direction)
    if not is_within_bounds(snake[0], play_area):
        print("Game Over: Snake hit the wall!")
        pygame.quit()
        sys.exit()

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


