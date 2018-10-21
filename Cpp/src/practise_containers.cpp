#include "practise_containers.h"
#include <sstream>
// stl::set
void create_set(){
	set<int> empty_set;
	empty_set.insert(10);
	empty_set.insert(20);
	empty_set.insert(30);
	empty_set.insert(40);
	empty_set.insert(60);
	empty_set.erase(20);
	set<int>::iterator it = empty_set.find(30);
	empty_set.erase(++it, empty_set.end());
	empty_set.insert(21);
	print_set(empty_set);


	int arr[] = {1,2,3,1,2,3};
	set<int> copy_set(arr, arr+6);
	print_set(copy_set);
	another_print_set(copy_set);
}

void another_print_set(const set<int>& i_set){
	for(const int& it : i_set){
		cout << it << " ";
	}
	cout << endl;

}
void print_set(const set<int>& i_set){
	ostringstream os;
	for(set<int>::const_iterator it = i_set.begin(), end = i_set.end(); it != end; ++it) {
		os << *it << " ";
	}
	cout << os.str() << endl;
}


void create_map(){
	map<string, string> my_map;
	my_map["1st_key"] = "The first value";
	my_map.insert(std::pair<string, string>("2nd_key", "The second value"));
	my_map["3rd_key"] = "The third value";
	my_map["4th_key"] = "The fourth value";
	if (my_map.count("1st_key")){
		cout << "True" << endl;
	} else {
		cout << "False" << endl;
	}

	print_map(my_map);
}

void print_map(const map<string, string>& i_map){
	for(map<string, string>::const_iterator it = i_map.begin(), end = i_map.end(); it != end; ++it){
		cout << "Map[" << it->first << "] = \"" << it->second << "\"" << endl;
	}
}
