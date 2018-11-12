#include <iostream>
#include <string>
#include "quiz_general.h"
using namespace std;

// CHECK ANAGRAMS
bool check_anagrams_iter(const string &s1, const string &s2){
	if(s1.length() != s2.length())
		return false;

	string temp = s2;
	for(int i1 = 0, len1 = s1.length(); i1 < len1; ++i1){
		bool found = false;
		int pos = 0;
		for(int i2 = 0, len2 = temp.length(); i2 < len2; ++i2){
			if(s1[i1] == temp[i2]){
				found = true;
				pos = i2;
				break;
			}
		}
		if (found == true){
			temp.erase(pos,1);
		} else {
			return false;
		}
	}
	return true;
}

bool check_anagrams_stack(const string &s1, const string &s2){
	if (s1.length() != s2.length())
		return false;

	const int ALPHABET_SIZE = 26;
	int arr_1[ALPHABET_SIZE] = {0};
	int arr_2[ALPHABET_SIZE] = {0};
	int a = 'a';
	for(int i = 0, len=s1.length(); i < len; ++i){
		int index = s1[i] - a;
		arr_1[index]++;
	}

	for(int i = 0, len=s2.length(); i < len; ++i){
		int index = s2[i] - a;
		arr_2[index]++;
	}

	for(int i = 0; i < 26; ++i){
		if(arr_1[i] != arr_2[i])
			return false;
	}
	return true;
}

// CHECK BALANCED PARENTHESE
#include <stack>
bool checkBalancedParenthese(string &input){
	stack<int> parStack;
	for(int i = 0, len = input.length(); i<len; ++i){
		if (input[i] == '(')
			parStack.push(1);
		else if (input[i] == ')'){
			if (parStack.empty())
				return false;
			else
				parStack.pop();
		}
	}
	return parStack.empty();
}
