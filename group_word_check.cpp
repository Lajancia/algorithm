#include<iostream>
#include<string>

using namespace std;

int main(){
	int number;
	string word;
	int sum=0;
	cin>> number;


	string a[number];

	for(int i=0;i<number;i++){
		cin>>a[i];
	}
	for(int n=0;n<number;n++){
		word=a[n];
		int count=0;
		bool t=true;
		for(int i=0;i<word.length();i++){
			count=0;
			for(int j=i;j<word.length();j++){
				if(word[i]!=word[j]){
					count=1;
				}
				else if(count==1&&word[j]==word[i]){
					t=false;

				}
			}
		}
		if(!t) sum +=0;
		else sum+=1;
	}
	cout<<sum;
	return 0;
}
