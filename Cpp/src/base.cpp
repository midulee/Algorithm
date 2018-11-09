#include <iostream>
#include <string>
#include "base.h"
std::string bool_to_string(const bool &in){
	return (in) ? "True" : "False";
}

void print_array(int arr[]){
	int i = 0;
	while (i < (sizeof(arr) / sizeof(arr[0]))){
		std::cout << arr[i] << " ";
	}
	std::cout << std::endl;
}




