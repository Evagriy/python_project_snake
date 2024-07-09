from typing import List, Tuple
from exceptions import tuple_exists_error

W = 1 #up
A = 2 #left
S = 3 #down
D = 4 #right

direction = (0, 1) #right

list_numbers = [(2, 4), (5, 7)]
new_tuple = (1, 2)
eating:  bool = True

def check_tuple(list_numbers: List[tuple[int, int]], new_tuple: Tuple[int, int]) -> bool:
    if new_tuple in list_numbers:
        raise tuple_exists_error("game over")

def change_direction(directionWASD, direction):
    if directionWASD == 1 and direction != (0, -1):
        direction = (0, 1)
    elif directionWASD == 2 and direction != (1, 0):
        direction = (-1, 0)
    elif directionWASD == 3 and direction != (0, 1):
        direction = (0, -1)
    elif directionWASD == 4 and direction != (-1, 0):
        direction = (1, 0)
    print(direction)

def add_tuple(new_tuple: Tuple[int, int]) -> None:

    try:
        check_tuple(list_numbers, new_tuple)
        list_numbers.append(new_tuple)
        print(f"tuple {new_tuple} add in list.")
    except tuple_exists_error as e:
        print(e)
        return

    if eating:
        print("Похавал")
    elif eating == False:
        del list_numbers[0]
        print("Голодуха")

    print(list_numbers)

add_tuple(new_tuple)
change_direction(D, direction)