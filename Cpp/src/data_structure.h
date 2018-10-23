#ifndef DATA_STRUCTURE_H
#define DATA_STRUCTURE_H

#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;


template<typename T>
void print_member(const T arr, const int& size);

void test();

void bench_mark(int n, void (*func)(int));
void loop(int n);
void loop_math(int n);
void test_function_pointer();
void create_random_list(int size);

#endif
