from typing import List, Tuple

list_numbers = [(2, 4), (5, 7)]
new_tuple = (1, 2)
eating:  bool = True

def check_tuple(list_numbers: List[tuple[int, int]], new_tuple: Tuple[int, int]) -> bool:
    return new_tuple in list_numbers

def add_tuple(new_tuple: Tuple[int, int]) -> None:

    list_numbers.append(new_tuple)
    print(check_tuple(list_numbers, new_tuple))
    if eating:
         del list_numbers[0]

    print(list_numbers)

add_tuple(new_tuple)