#include "data_structure.h"
#include <string>
#include <set>

void test(){
	int arr[6] = {1,3,5,4,2,6};
	string str[] = {"Hello", "the", "world"};
	print_member(arr, sizeof(arr)/sizeof(int));
	print_member(str, sizeof(str)/sizeof(string));
	set<int> myset;
}

template<typename T>
void print_member(const T& arr, const int& size) {
	string output;
	ostringstream os;
	for (int i = 0; i < size; i++) {
		os << arr[i] << " ";
	}
	cout << os.str() << endl;
}

