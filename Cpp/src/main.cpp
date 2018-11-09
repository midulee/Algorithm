#include "data_structure.h"
#include "practise_containers.h"
#include "quiz/quiz_general.h"
#include "base.h"
#include "quiz/sorting.h"

using namespace std;
int main(){
	bench_mark(10000, loop_math);
	bench_mark(10000, loop);
	create_random_list(10);

	string s1 = "efaacasdasadasdasdsadsada";
	string s2 = "efaacasdasedasdasdsadsada";
	cout << bool_to_string(check_anagrams_iter(s1,s2))<< endl;
	cout << bool_to_string(check_anagrams_stack(s1,s2))<< endl;

	int unsortArray[] = {6,3,2,5,1,4};
	merge_sort(unsortArray, 6);
	print_member(unsortArray, 6);
	return 0;
}
