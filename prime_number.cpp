#include<iostream>


using namespace std;

int main(){

	int X;
	int Y;
	int sum=0;
	int count=0;
	int min=0;
	cin>>X;
	cin>>Y;

	for(int i=X;i<Y+1;i++){
		if(i==1)
			continue;
		else if(i==2){
			sum=sum+i;
			count+=1;
			if(count==1)
				min=sum;
			continue;
		}

		else if(i%2==0){
			continue;
		}
		int time=0;
		for(int k=2;k<i;k++){
			if(i%k==0)
				time+=1;
		}
		if(time==0){
			sum=sum+i;
			count+=1;
		}
		if(count==1)
			min=sum;
	}
	if(count==0){
		cout<<-1;
		return 0;
	}
	cout<<sum<<endl;
	cout<<min<<endl;
	return 0;
}
