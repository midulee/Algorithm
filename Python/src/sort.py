import inspect
class Sort:
    def __init__(self, input):
        self.list = list(input)
        self.given = list(input)

    def restore(self):
        self.list = self.given

    def print_sorted_list(self):
        print(self.list)

    def swap(self, first_index, second_index):
        self.list[first_index], self.list[second_index] = self.list[second_index], self.list[first_index]

    # Merge sort
    def merge_left_and_right(self, left, right):
        i_left, i_right = 0,0
        len_left, len_right = len(left), len(right)
        merged_list = []
        while len(merged_list) < (len_left + len_right):
            if left[i_left] <= right[i_right]:
                merged_list.append(left[i_left])
                i_left += 1
            else:
                merged_list.append(right[i_right])
                i_right += 1
            if (i_left == len_left) and i_right < len_right:
                merged_list = merged_list + right[i_right:]
                break
            elif (i_right == len_right) and i_left < len_left:
                merged_list = merged_list + left[i_left:]
                break
        return merged_list

    def merge_sort_recursive(self, in_list):
        if len(in_list) <= 1:
            return in_list
        mid = len(in_list) // 2
        left = self.merge_sort_recursive(in_list[:mid])
        right = self.merge_sort_recursive(in_list[mid:])
        return self.merge_left_and_right(left, right)

    def merge_sort(self):
        out = self.merge_sort_recursive(self.list)
        self.list = out

    def bubble_sort(self):
        top = len(self.list)
        while True:
            has_swap = False
            for i in range(top - 1):
                if self.list[i] > self.list[i + 1]:
                    self.swap(i, i+1)
                    has_swap = True
            else:
                if not has_swap:
                    break
            top -= 1

    def selection_sort(self):
        print("SELECTION SORT")
        for index in range(len(self.list)):
            # Find smallest index in the list
            min = index
            for i in range(index, len(self.list), 1):
                if self.list[i] < self.list[min]:
                    min = i

            # Swap smallest member with current index
            if min != index: # index is not smallest
                self.swap(min, index)
            self.print_sorted_list()

    def insertion_sort(self):
        print(inspect.stack()[0][3])
        for index in range(len(self.list)):
            temp = self.list[index]
            for i in range(index-1, -1, -1):
                if temp < self.list[i]:
                    self.swap(i, i+1)
                else:
                    self.list[i+1] = temp
                    break
            self.print_sorted_list()