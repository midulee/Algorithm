/*
 * dp.h
 *
 *  Created on: Nov 11, 2018
 *      Author: xleeduc
 */

#ifndef SRC_QUIZ_DP_H_
#define SRC_QUIZ_DP_H_
#include <string>
#include <unordered_map>
int find_LCS_length(const std::string &s1, const std::string &s2);
int find_LCS_length_impl(const std::string &s1, const std::string &s2,
		int l1, int l2, std::unordered_map<std::string, int>);



#endif /* SRC_QUIZ_DP_H_ */
