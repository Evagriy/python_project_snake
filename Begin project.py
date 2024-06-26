from typing import List, Tuple

list_numbers = [(2, 4), (5, 7)]
new_tuple = (1, 2)
eating:  bool = True

class tuple_exists_error(Exception):
    pass


def check_tuple(list_numbers: List[tuple[int, int]], new_tuple: Tuple[int, int]) -> bool:
    if new_tuple in list_numbers:
        raise tuple_exists_error("game over")
    return False

def add_tuple(new_tuple: Tuple[int, int]) -> None:

    try:
        check_tuple(list_numbers, new_tuple)
        list_numbers.append(new_tuple)
        print(f"tuple {new_tuple} add in list.")
    except tuple_exists_error as e:
        print(e)
        return

    if eating == True:
        print("Похавал")
    elif eating == False:
        del list_numbers[0]
        print("Голодуха")

    print(list_numbers)

add_tuple(new_tuple)