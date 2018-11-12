#include "data_structure.h"
#include <string>
#include <set>
#include <ctime>
#include <random>

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
