class Sort:
    def __init__(self, input):
        self.input = input

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
        out = self.merge_sort_recursive(self.input)
        self.input = out

    def print_sorted_list(self):
        print(self.input)
