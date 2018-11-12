/*
 * base.h
 *
 *  Created on: Nov 5, 2018
 *      Author: xleeduc
 */

#ifndef SRC_BASE_H_
#define SRC_BASE_H_
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

std::string bool_to_string(const bool &in);

template <typename T>
void unit_test(bool (*func)(T&), std::vector<T> testcase){
	for (int i = 0; i < testcase.size(); ++i){
		std::cout << func(testcase[i]) << "; ";
	}
}

template <typename T>
void bench_mark(T n, void (*func)(T)){
	clock_t start = clock();
	func(n);
	clock_t end = clock();
	double elapsed_time = double(end - start ) / CLOCKS_PER_SEC;
	std::cout << elapsed_time << std::endl;
}

template <typename T>
void bench_mark(T n, T n1, void (*func)(T, T)){
	clock_t start = clock();
	func(n, n1);
	clock_t end = clock();
	double elapsed_time = double(end - start ) / CLOCKS_PER_SEC;
	std::cout << elapsed_time << std::endl;
}

template<typename T>
void print_member(const T arr, const int& size){
	std::string output;
	std::ostringstream os;
	for (int i = 0; i < size; i++) {
		os << arr[i] << " ";
	}
	std::cout << os.str() << std::endl;
}
#endif /* SRC_BASE_H_ */
