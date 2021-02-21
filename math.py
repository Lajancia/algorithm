def eratos(n):
		N=n
		M=1
		li=[]
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
		for k in range(M,N+1):
				if num_range[k]:
					li.append(k)
		return li

num=int(input())

if(num==1):
		print('')
		
else:
		li=eratos(num)
		#print(li)
		
		result=num
		b=True
		count=0
		while(b):
			if(result/li[count]==1):
				print(li[count])
				break
			elif(result%li[count]==0):
				result=result/li[count]
				print(li[count])
			else:
				count=count+1
		