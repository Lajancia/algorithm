#include<iostream>


using namespace std;

int main(){

	int num;
	int H,W,N;
	int a=0,b=0;

	cin>>num;
	for(int i=0;i<num;i++){
		cin>>H>>W>>N;

		if(H==1){
			a=H;
			b=N;
			if(b<10)
				cout<<a<<0<<b<<endl;
			else
				cout<<a<<b<<endl;
			continue;
		}
		
		else if(N%H==0){
			a=H;
			b=N/H;
			if(b<10)
				cout<<a<<0<<b<<endl;
			else
				cout<<a<<b<<endl;
		}
		else{
		b=N/H+1;
		a=N%H;
		if(b<10)
			cout<<a<<0<<b<<endl;
		else
			cout<<a<<b<<endl;
		}
	}

	return 0;
}

