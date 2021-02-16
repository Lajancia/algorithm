#include<iostream>
#include<string>

using namespace std;

int main(){
	string word;
	int sum=0;
	cin>> word;

	for(int i=0; i<word.length();i++){
	if(word[i]=='c'){
		if((i+1)!=word.length() && word[i+1]=='='){
			i+=1;
			sum+=1;
		}
		else if((i+1)!=word.length() && word[i+1]=='-'){
			i+=1;
			sum+=1;
		}
		else sum+=1;
	}

	else if(word[i]=='d'){
		if((i+2)!=word.length() && word[i+1]=='z'&& word[i+2]=='='){
					i+=2;
					sum+=1;
				}
		else if((i+1)!=word.length() && word[i+1]=='-'){
			i+=1;
			sum+=1;
		}
		else sum+=1;

	}

	else if(word[i]=='l'){
		if((i+1)!=word.length() && word[i+1]=='j'){
					i+=1;
					sum+=1;
				}
		else sum+=1;
	}

	else if(word[i]=='n'){
		if((i+1)!=word.length() && word[i+1]=='j'){
					i+=1;
					sum+=1;
				}
		else sum+=1;
	}

	else if(word[i]=='s'){
		if((i+1)!=word.length() && word[i+1]=='='){
					i+=1;
					sum+=1;
				}
		else sum+=1;
	}

	else if(word[i]=='z'){
		if((i+1)!=word.length() && word[i+1]=='='){
					i+=1;
					sum+=1;
				}
		else sum+=1;
	}

	else sum+=1;

	}

	cout<<sum;
	return 0;
}


