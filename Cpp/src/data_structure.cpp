#include "data_structure.h"
#include <string>
#include <set>
#include <ctime>
#include <random>

void test(){
	int arr[6] = {1,3,5,4,2,6};
	string str[] = {"Hello", "the", "world"};
	print_member(arr, sizeof(arr)/sizeof(int));
	print_member(str, sizeof(str)/sizeof(string));
}

template<typename T>
void print_member(const T arr, const int& size) {
	string output;
	ostringstream os;
	for (int i = 0; i < size; i++) {
		os << arr[i] << " ";
	}
	cout << os.str() << endl;
}

void bench_mark(int n, void (*func)(int)){
	clock_t start = clock();
	func(n);
	clock_t end = clock();
	double elapsed_time = double(end - start ) / CLOCKS_PER_SEC;
	cout << elapsed_time << endl;
}

void loop(int n){
	int sum = 0;
	for (int i = 1; i <= n; i++){
		sum += i;
	}
	cout << "Sum1 = " << sum << endl;
}

void loop_math(int n){
	int sum = n * (n + 1) / 2;
	cout << "Sum2 = " << sum << endl;
}

void create_random_list(int size){
	srand(time(NULL));
	std::vector<int> my_rand_vector;
	while (size-- > 0){
		int num = rand() % 100;
		my_rand_vector.push_back(num);
	}
	for(int i : my_rand_vector){
		cout << i << " " ;
	}
	cout << endl;

}
