from typing import List, Tuple

list_numbers = [(2, 4), (5, 7)]
new_tuple = (1, 2)
eating:  bool = False
not_eating: bool = True
def add_tuple(new_tuple: Tuple[int, int]) -> None:

    list_numbers.append(new_tuple)
    if not_eating:
        del list_numbers[0]

    print(list_numbers)

add_tuple(new_tuple)