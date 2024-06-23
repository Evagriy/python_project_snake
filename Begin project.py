from typing import List, Tuple

number_tuple = Tuple[int, int]

list_numbers = [(2, 4), (5, 7)]
new_tuple = (1, 2)

def add_tuple(new_tuple: number_tuple) -> None:

    list_numbers.append(new_tuple)
    del list_numbers[0]
    print(list_numbers)

add_tuple(new_tuple)