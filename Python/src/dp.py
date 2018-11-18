from mmap import mmap

from src.base import bench_mark

@bench_mark
def find_LCS_length_topdown(s1, s2, mmap):
    l1 = len(s1)
    l2 = len(s2)
    if l1 == 0 or l2 == 0:
        return 0;

    key = "{}_{}".format(l1,l2)
    if key in mmap:
        return mmap[key]

    if s1[l1-1] == s2[l2-1]:
        mmap[key] = 1 + find_LCS_length_topdown(s1[:l1 - 1], s2[:l2 - 1], mmap)
    else:
        mmap[key] = max(find_LCS_length_topdown(s1, s2[:l2 - 1], mmap), find_LCS_length_topdown(s1[:l1 - 1], s2, mmap))

    return mmap[key]

@bench_mark
def find_LCS_length_bottomup(s1, s2):
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


def longest_palindromic_sequence_topdown(seq, mmap):
    if len(seq) <= 1:
        return len(seq)
    if seq not in mmap:
        if seq[0] == seq[-1]:
            new_seq = seq[1:-1]
            mmap[seq] = longest_palindromic_sequence_topdown(new_seq, mmap) + 2
        else:
            left = longest_palindromic_sequence_topdown(seq[1:], mmap)
            right = longest_palindromic_sequence_topdown(seq[:-1], mmap)
            mmap[seq] = max(left, right)
    return mmap[seq]

