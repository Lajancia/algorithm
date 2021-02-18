N=10000

M=1
num_range=[True]*(N+1)

num_range[0]=False
num_range[1]=False

i=2

while i<=N**(1/2)+1:
		if num_range[i]==True:
			j=i*i
			while j<=N:
				num_range[j]=False
				j+=i
		i+=1
count=0
for k in range(M,N+1):
		if num_range[k]:
			count +=1

num=int(input())

for i in range(num):
		n=int(input())
		for j in range(n//2,1,-1):
			if num_range[j]:
				if(num_range[n-j]):
					print(j, end=' ')
					print(n-j)
					break;