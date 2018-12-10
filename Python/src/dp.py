from mmap import mmap
import sys

from src.base import bench_mark

@bench_mark
def find_LCS_length_td(s1, s2, mmap):
    l1 = len(s1)
    l2 = len(s2)
    if l1 == 0 or l2 == 0:
        return 0;

    key = "{}_{}".format(l1,l2)
    if key in mmap:
        return mmap[key]

    if s1[l1-1] == s2[l2-1]:
        mmap[key] = 1 + find_LCS_length_td(s1[:l1 - 1], s2[:l2 - 1], mmap)
    else:
        mmap[key] = max(find_LCS_length_td(s1, s2[:l2 - 1], mmap), find_LCS_length_td(s1[:l1 - 1], s2, mmap))

    return mmap[key]

@bench_mark
def find_LCS_length_bu(s1, s2):
    #Intialize zeros table
    l1 = len(s1)+1
    l2 = len(s2)+1
    table = [[0] * l2 for i in range(l1)]
    for i1 in range(1, l1):
        for i2 in range(1, l2):
            if s1[i1-1] == s2[i2-1]:
                table[i1][i2] = table[i1][i2-1] + 1
            else:
                table[i1][i2] = max(table[i1-1][i2], table[i1][i2-1])

    return table[l1-1][l2-1]

def find_ugly_number(nth):
    ugly = [1] * nth
    i = 1
    i_2, i_3, i_5 = 0,0,0
    ugly_2 = ugly[i_2] * 2
    ugly_3 = ugly[i_3] * 3
    ugly_5 = ugly[i_5] * 5
    while i < nth:
        ugly[i] = min(ugly_2, ugly_3, ugly_5)
        if ugly[i] == ugly_2:
            i_2 += 1
            ugly_2 = ugly[i_2] * 2
        if ugly[i] == ugly_3:
            i_3 += 1
            ugly_3 = ugly[i_3] * 3
        if ugly[i] == ugly_5:
            i_5 += 1
            ugly_5 = ugly[i_5] * 5
        i += 1
    print(ugly)
    print(ugly[-1])

def longest_increase_sequence(arr):
    table = [1] * len(arr)
    for i in range(1, len(arr), 1):
        for j in range(i):
            if arr[j] < arr[i]:
                table[i] = max(table[i], table[j] + 1)
    print(max(table))


def longest_palindromic_sequence_td(seq, mmap):
    if len(seq) <= 1:
        return len(seq)
    if seq not in mmap:
        if seq[0] == seq[-1]:
            new_seq = seq[1:-1]
            mmap[seq] = longest_palindromic_sequence_td(new_seq, mmap) + 2
        else:
            left = longest_palindromic_sequence_td(seq[1:], mmap)
            right = longest_palindromic_sequence_td(seq[:-1], mmap)
            mmap[seq] = max(left, right)
    return mmap[seq]


def get_minimum_coin_to_reach_target_td(target, mem):
    if mem[target]:
        return mem[target]

    if target < 0:
        return sys.maxsize
    elif target > 0:
        mem[target] = 1 + min(get_minimum_coin_to_reach_target_td(target - 1, mem),
                              get_minimum_coin_to_reach_target_td(target - 2, mem),
                              get_minimum_coin_to_reach_target_td(target - 5, mem))
        return mem[target]
    else:
        return 0


def get_minimum_coin_to_reach_target_bu(target, coins):
    table = [0] * (target+1)
    for i in range(1, target+1):
        table[i] = min([table[i-c] + 1 for c in coins if i >= c])
    return table[target]


'''
This problem is called the string edit distance problem, and is quite useful in many areas of research. 
Suppose that you want to transform the word “algorithm” into the word “alligator.” 
For each letter you can either copy the letter from one word to another at a cost of 5, 
you can delete a letter at cost of 20, or insert a letter at a cost of 20. 
The total cost to transform one word into another is used by spell check programs 
to provide suggestions for words that are close to one another. 
Use dynamic programming techniques to develop an algorithm that 
gives you the smallest edit distance between any two words.


  1        2           3
  2        3           4
  3        4           8
  4        5           8
  5        9          10

'''

def max_profit_in_limitation_bu(limit):
    items = [{'weight': 2, 'value': 3},
             {'weight': 3, 'value': 4},
             {'weight': 4, 'value': 8},
             {'weight': 5, 'value': 8},
             {'weight': 9, 'value': 10}]
    profit_table = [0] * limit
