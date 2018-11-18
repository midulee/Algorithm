from src.data_structure import Stack, LinkedList
from src.sort import Sort
import src.dp as dp
import random
import src.misc as misc




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
    misc.test_misc()

    ll = LinkedList()
    for i in range(10):
        ll.add(i)
    ll.print_list()
    ll.remove(3)
    ll.remove(9)
    ll.remove(0)
    ll.print_list()
