import sys
from typing import List, Tuple
from exceptions import TupleExistsError, OutOfBoundsError
import pygame
import main

pygame.init()

W = 1 #up
A = 2 #left
S = 3 #down
D = 4 #right

direction = (0, 1) #right

screen_area = (500, 500)
play_area = (20, 20)
list_numbers = [(2, 4), (5, 7)]
new_tuple = (1, 2)
eating:  bool = True

screen = pygame.display.set_mode(screen_area)
pygame.display.set_caption("ИГРА ЗМЕЙКА  0_o")
jpg = pygame.image.load("snake.jpg")
pygame.display.set_icon(jpg)
screen.fill((255, 255, 255))

turquoise = (0, 255, 204)
white = (255, 255, 255)
blue = (204, 255, 255)
width = heigth = 20
margin = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill(turquoise)
    for coloumn in range(play_area[0]):
        for row in range(play_area[1]):
            if (row + coloumn) % 2 == 0:
                color = blue
            else:
                color = white
            x = 40 + coloumn * width + margin * (coloumn + 1)
            y = 40 + row * heigth + margin * (row + 1)
            pygame.draw.rect(screen, color,(x, y, width, heigth))
    pygame.display.update()

    keys = pygame.key.get_pressed()

    def change_direction(direction, keys):
        if keys[pygame.K_UP] and direction != (0, 1):
            direction = (0, -1)
        elif keys[pygame.K_LEFT] and direction != (1, 0):
            direction = (-1, 0)
        elif keys[pygame.K_DOWN] and direction != (0, -1):
            direction = (0, 1)
        elif keys[pygame.K_RIGHT] and direction != (-1, 0):
            direction = (1, 0)
        print()
        print("change of direction to:")
        print(direction)




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


try:
    add_tuple(list_numbers, new_tuple, eating, play_area)
except OutOfBoundsError as e:
    print(e)
change_direction(direction, keys)
### исправил говно ###