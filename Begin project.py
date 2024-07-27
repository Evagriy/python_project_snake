from typing import List, Tuple
from exceptions import tuple_exists_error, out_of_bounds_error

W = 1 #up
A = 2 #left
S = 3 #down
D = 4 #right

direction = (0, 1) #right

play_area = (50, 50)
list_numbers = [(2, 4), (5, 7)]
new_tuple = (1, 2)
eating:  bool = True

def check_tuple(list_numbers: List[tuple[int, int]], new_tuple: Tuple[int, int]) -> bool:
    if new_tuple in list_numbers:
        raise tuple_exists_error("game over")

def is_within_bounds(new_tuple: Tuple[int, int], play_area: Tuple[int, int]) -> bool:
    x, y = new_tuple
    width, height = play_area
    return 0 <= x < width and 0 <= y < height

def change_direction(directionWASD, direction):
    if directionWASD == 1 and direction != (0, 1):
        direction = (0, -1)
    elif directionWASD == 2 and direction != (1, 0):
        direction = (-1, 0)
    elif directionWASD == 3 and direction != (0, -1):
        direction = (0, 1)
    elif directionWASD == 4 and direction != (-1, 0):
        direction = (1, 0)
    print()
    print("change of direction to:")
    print(direction)

def add_tuple(list_numbers: List[Tuple[int, int]], new_tuple: Tuple[int, int], eating: bool, play_area: Tuple[int, int]) -> None:
    if not is_within_bounds(new_tuple, play_area):
        raise out_of_bounds_error(f"Tuple {new_tuple} is out of bounds for play area {play_area}")

    try:
        check_tuple(list_numbers, new_tuple)
        list_numbers.append(new_tuple)
        print(f"tuple {new_tuple} add in list.")
    except tuple_exists_error as e:
        print(e)
        return
    except out_of_bounds_error as e:
        print(e)
        return

    if eating:
        print("Похавал")
    elif eating == False:
        del list_numbers[0]
        print("Голодуха")

    print(list_numbers)

try:
    add_tuple(list_numbers, new_tuple, eating, play_area)
except out_of_bounds_error as e:
    print(e)
change_direction(A, direction)