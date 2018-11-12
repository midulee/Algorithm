/*
 * dp.cpp
 *
 *  Created on: Nov 11, 2018
 *      Author: xleeduc
 */
#include "dp.h"
#include <unordered_map>

int find_LCS_length_impl(const std::string &s1, const std::string &s2, int l1, int l2, std::unordered_map<std::string, int> mmap){
	if (l1 == 0 || l2 == 0)
		return 0;
	std::string key = l1 + "_" + l2;
	if (mmap[key])
		return mmap[key];
	if (s1[l1-1] == s2[l2-1])
		mmap[key] = 1 + find_LCS_length_impl(s1, s2, l1-1, l2-1, mmap);
	else {
		int first = find_LCS_length_impl(s1, s2, l1-1, l2, mmap);
		int second = find_LCS_length_impl(s1, s2, l1, l2-1, mmap);
		mmap[key] = (first > second) ? first : second;
	}
	return mmap[key];
}

int find_LCS_length(const std::string &s1, const std::string &s2){
	int l1 = s1.length();
	int l2 = s2.length();
	std::unordered_map<std::string, int> memorization;
	return find_LCS_length_impl(s1, s2, l1, l2, memorization);
}


