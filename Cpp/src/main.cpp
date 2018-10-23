#include "data_structure.h"
#include "practise_containers.h"
int main(){
	bench_mark(10000, loop_math);
	bench_mark(10000, loop);
	create_random_list(10);
	return 0;
}
