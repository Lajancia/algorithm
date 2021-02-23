num=int(input())

for i in range(num):
	a1, b1, c1, a2, b2, c2=map(int,input().split())

	m=((a1-a2)**2+(b1-b2)**2)**(1/2)
	n=((c1+c2)**2)**(1/2)
	n2=((c1-c2)**2)**(1/2)
	if(n2<m and n>m):
		print(2)
		
	elif(n==m):
		print(1)
	elif(m==0 and n2==0):
		print(-1)
	elif(n2==m):
		print(1)

	else:
		print(0)