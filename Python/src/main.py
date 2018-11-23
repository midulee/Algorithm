from src.data_structure import Stack, LinkedList
from src.sort import Sort
from src.Drawable import Drawable
import src.dp as dp
import random
import src.misc as misc

def sort_func():
    ran_list = [random.randint(0, 100) for _ in range(10)]
    print(ran_list)
    sort = Sort(ran_list)
    sort.merge_sort()
    sort.print_sorted_list()

def dynamic_programming_func():
    s1 = "ABCBDABA"
    s2 = "BDCABA"
    mmap = {}
    print(dp.find_LCS_length_topdown(s1, s2, mmap))
    print(dp.find_LCS_length_bottomup(s1, s2))

    dp.find_ugly_number(15)
    print("Longest increasing sequence")
    dp.longest_increase_sequence([10,22,9,33,21,50,41,60])
    print("Longest palindromic sequence")
    seq = "ABBDACAB"
    mmap = {}
    print(dp.longest_palindromic_sequence_topdown(seq, mmap))

    print("Coin change to reach target")
    target = 19
    mem = [0] * (target + 1)
    print(dp.get_minimum_coin_to_reach_target_topdown(target, mem))
    print(dp.get_minimum_coin_to_reach_target_bottomup(10, [1,2,5]))


def data_structure_func():
    # Data structure
    def stack():
        stack = Stack([1,2,4])
        stack.push(3)
        stack.push(5)
        stack.print()
        stack.pop()
        stack.print()
    stack()

    def linked_list():
        ll = LinkedList()
        for i in range(10):
            ll.add(i)
        ll.print_list()
        ll.remove(3)
        ll.remove(9)
        ll.remove(0)
        ll.print_list()
    linked_list()

def misc_func():
    misc.test_misc()


def draw_func():
    # Draw part
    paint = Drawable()
    paint.main()

if __name__ == '__main__':
    # data_structure_func()
    # dynamic_programming_func()
    # sort_func()
    # misc_func()
    draw_func()

