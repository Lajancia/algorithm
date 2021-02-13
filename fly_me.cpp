#include<iostream>


using namespace std;

int main(){

	int num;
	int X,Y;

	cin>>num;


	for(int m=0;m<num;m++){
		cin>>X>>Y;
		long sum=2;
		long sum1=2;
		int count=2;

		if(Y-X==1){
			cout<<1<<endl;
			continue;
		}
		else if(Y-X==2){
			cout<<2<<endl;
			continue;
		}


		for(int i=2;;i++){
			sum1=sum1+i;
			count+=1;
			if((Y-X)>sum&&(Y-X)<=sum1){
				cout<<count<<endl;
				break;
			}

			sum=sum1;
			sum1=sum1+i;
			count+=1;
			if((Y-X)>sum&&(Y-X)<=sum1){
				cout<<count<<endl;
				break;
			}

	}
	}

	return 0;
}