from src.data_structure import Stack
from src.sort import Sort
import random

if __name__ == '__main__':
    ran_list = [random.randint(0, 100) for _ in range(10)]
    print(ran_list)
    sort = Sort(ran_list)
    sort.merge_sort()
    sort.print_sorted_list()

    stack = Stack([1,2,4])
    stack.push(3)
    stack.push(5)
    stack.print()
    stack.pop()
    stack.print()