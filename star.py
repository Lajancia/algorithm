num=int(input())

li=[['*' for i in range(num)]for j in range(num)]

def star(li,num,real):
		n=num//3
		temp=li
		if(num==1):
			return temp
		
		else:
			#print(2)
			for i in range(real):
				for j in range(real):
					if((i%num>=n) and (i%num<2*n)) and ((j%num>=n) and (j%num<2*n)):
						temp[i][j]=' '
						#print(1)
			n=n//3
			for i in range(real):
				for j in range(real):
					if((i%num>=n) and (i%num<2*n)) and ((j%num>=n) and (j%num<2*n)):
						temp[i][j]=' '
			return star(temp,num//3,real)

li=star(li,num,num)
for i in range(num):
		for j in range(num):
			print(li[i][j],end='')
		print()
		
