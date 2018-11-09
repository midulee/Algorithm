/*
 * sorting.cpp
 *
 *  Created on: Nov 6, 2018
 *      Author: xleeduc
 */
#include <iostream>
#include "sorting.h"

void merge_2_part(int input[], int begin, int mid, int end){
	int s_left = mid - begin + 1;
	int s_right = end - mid;
	int left[s_left];
	int right[s_right];

	int j = 0, k = 0;
	for(int i = begin; i <= end; ++i){
		if (i < mid+1)
			left[j++] = input[i];
		else
			right[k++] = input[i];
	}

	k = j = 0;
	while(begin <= end){
		if (j < s_left and k < s_right){
			if (left[j] <= right[k])
				input[begin++] = left[j++];
			else
				input[begin++] = right[k++];
		} else if (j < s_left){
			input[begin++] = left[j++];
		} else {
			input[begin++] = right[k++];
		}
	}
}

void merge_sort(int input[], int begin, int end){
	if (begin < end){
		int mid = begin + (end - begin) / 2;
		merge_sort(input, begin, mid);
		merge_sort(input, mid+1, end);
		merge_2_part(input, begin, mid, end);
	}
	return;
}

void merge_sort(int input[], int size){
	merge_sort(input, 0, size-1);
}

